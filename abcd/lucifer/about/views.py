from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Review, Cart, CartItem, Order, OrderItem
from .sms_service import send_order_confirmation_sms
from django.utils.text import slugify
from datetime import datetime
import random

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    
    # Handle review submission
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if rating and comment:
            try:
                Review.objects.update_or_create(
                    product=product,
                    user=request.user,
                    defaults={'rating': int(rating), 'comment': comment}
                )
                messages.success(request, 'Review submitted successfully!')
                return redirect('product_detail', product_id=product_id)
            except Exception as e:
                messages.error(request, f'Error submitting review: {str(e)}')
        else:
            messages.error(request, 'Please provide both rating and comment.')
    
    # Get similar products (same category or similar name)
    similar_products = Product.objects.exclude(id=product_id).order_by('?')[:3]
    
    average_rating = product.get_average_rating()
    
    context = {
        'product': product,
        'reviews': reviews,
        'similar_products': similar_products,
        'average_rating': average_rating,
    }
    
    return render(request, 'product_detail.html', context)

@login_required(login_url='login')
def admin_dashboard(request):
    products = Product.objects.all()
    return render(request, 'admin_dashboard.html', {'products': products})

@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        if not name or not description or not price:
            messages.error(request, 'All fields are required.')
            return render(request, 'add_product.html')
        
        try:
            product = Product.objects.create(
                name=name,
                description=description,
                price=float(price),
                image=image
            )
            messages.success(request, f'Product "{name}" added successfully!')
            return redirect('admin_dashboard')
        except Exception as e:
            messages.error(request, f'Error adding product: {str(e)}')
    
    return render(request, 'add_product.html')

@login_required(login_url='login')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        product.price = request.POST.get('price', product.price)
        
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        try:
            product.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('admin_dashboard')
        except Exception as e:
            messages.error(request, f'Error updating product: {str(e)}')
    
    return render(request, 'edit_product.html', {'product': product})

@login_required(login_url='login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_name = product.name
    product.delete()
    messages.success(request, f'Product "{product_name}" deleted successfully!')
    return redirect('admin_dashboard')

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    customization = request.POST.get('customization', '')
    
    try:
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            customization=customization
        )
        if not item_created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f'{product.name} added to cart!')
    except Exception as e:
        messages.error(request, f'Error adding to cart: {str(e)}')
    
    return redirect('view_cart')

@login_required(login_url='login')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = cart.get_total()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
    }
    
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.cart.user == request.user:
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f'{product_name} removed from cart!')
    
    return redirect('view_cart')

@login_required(login_url='login')
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.cart.user == request.user:
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
    
    return redirect('view_cart')

@login_required(login_url='login')
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    
    if not cart_items:
        messages.error(request, 'Your cart is empty!')
        return redirect('view_cart')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        
        if not all([name, email, phone, address, city, state, zipcode]):
            messages.error(request, 'All fields are required.')
            return render(request, 'checkout.html', {
                'cart': cart,
                'cart_items': cart_items,
                'total': cart.get_total(),
            })
        
        try:
            order_number = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
            
            order = Order.objects.create(
                user=request.user,
                order_number=order_number,
                total_amount=cart.get_total(),
                name=name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                zipcode=zipcode,
                status='pending'
            )
            
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                    customization=item.customization
                )
            
            cart_items.delete()
            
            # Send SMS confirmation to customer
            sms_sent = send_order_confirmation_sms(order)
            
            if sms_sent:
                messages.success(request, f'Order placed successfully! Order number: {order_number}. Confirmation SMS sent to {phone}')
            else:
                messages.success(request, f'Order placed successfully! Order number: {order_number}')
            
            return redirect('order_confirmation', order_id=order.id)
        
        except Exception as e:
            messages.error(request, f'Error placing order: {str(e)}')
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total': cart.get_total(),
        'user': request.user,
    }
    
    return render(request, 'checkout.html', context)

@login_required(login_url='login')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if order.user != request.user:
        messages.error(request, 'Unauthorized access.')
        return redirect('home')
    
    context = {
        'order': order,
        'order_items': order.items.all(),
    }
    
    return render(request, 'order_confirmation.html', context)

@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
    }
    
    return render(request, 'my_orders.html', context)

def about(request):
    return render(request, 'about.html')