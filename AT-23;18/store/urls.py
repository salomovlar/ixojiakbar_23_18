from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/like/', views.like_book, name='like_book'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/books/', views.admin_books, name='admin_books'),
    path('admin/books/add/', views.add_book, name='add_book'),
    path('admin/books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('admin/books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/orders/<int:order_id>/update/', views.update_order_status, name='update_order_status'),
]
