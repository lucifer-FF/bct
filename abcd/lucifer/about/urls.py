from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('products', views.products_view, name='products'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    
    # Cart and Checkout
    path('cart', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>', views.update_cart_item, name='update_cart_item'),
    path('checkout', views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>', views.order_confirmation, name='order_confirmation'),
    path('my-orders', views.my_orders, name='my_orders'),
    
    # Admin
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add', views.add_product, name='add_product'),
    path('admin/edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('admin/delete/<int:product_id>', views.delete_product, name='delete_product'),
]