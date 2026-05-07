from django.contrib import admin
from .models import Book, BookLike, Order, OrderItem, Cart, CartItem, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author', 'description')
    date_hierarchy = 'created_at'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'full_name', 'phone')
    inlines = [OrderItemInline]
    actions = ['mark_as_accepted', 'mark_as_rejected', 'mark_as_completed']

    def mark_as_accepted(self, request, queryset):
        queryset.update(status='accepted')
    mark_as_accepted.short_description = "Buyurtmani qabul qilingan deb belgilash"

    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')
    mark_as_rejected.short_description = "Buyurtmani rad etilgan deb belgilash"

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Buyurtmani yakunlangan deb belgilash"

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'book', 'quantity', 'price')

@admin.register(BookLike)
class BookLikeAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('book__title', 'user__username')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'book', 'quantity')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'address', 'phone')
