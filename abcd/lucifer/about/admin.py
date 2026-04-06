from django.contrib import admin
from .models import Product, Review, Cart, CartItem, Order, OrderItem, SMSNotification

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-created_at']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    search_fields = ['product__name', 'user__username', 'comment']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__username']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'updated_at']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class SMSNotificationInline(admin.TabularInline):
    model = SMSNotification
    extra = 0
    readonly_fields = ['created_at', 'updated_at', 'twilio_sid']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'total_amount', 'status', 'created_at']
    search_fields = ['order_number', 'user__username', 'email']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline, SMSNotificationInline]
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    ordering = ['-created_at']

class SMSNotificationAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'notification_type', 'status', 'created_at']
    search_fields = ['phone_number', 'order__order_number']
    list_filter = ['status', 'notification_type', 'created_at']
    readonly_fields = ['phone_number', 'message', 'notification_type', 'twilio_sid', 'created_at', 'updated_at']
    ordering = ['-created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(SMSNotification, SMSNotificationAdmin)
