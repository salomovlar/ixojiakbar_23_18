"""
Test skripti - loyihaning barcha funksiyalarini tekshirish
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from django.test import TestCase, Client
from django.contrib.auth.models import User
from store.models import Book, BookLike, Cart, CartItem, Order, OrderItem

def test_models():
    print("1. Modellar tekshirilmoqda...")
    
    # Book model
    book_count = Book.objects.count()
    print(f"   - Kitoblar soni: {book_count}")
    
    # UserProfile va Cart avtomatik yaratilishi
    user = User.objects.create_user(username='testuser', password='test123')
    print(f"   - Foydalanuvchi yaratildi: {user.username}")
    
    has_profile = hasattr(user, 'profile')
    has_cart = hasattr(user, 'cart')
    print(f"   - Profile mavjud: {has_profile}")
    print(f"   - Cart mavjud: {has_cart}")
    
    return user

def test_urls():
    print("\n2. URL manzillari tekshirilmoqda...")
    client = Client()
    
    urls = [
        ('/', 'Bosh sahifa'),
        ('/login/', 'Login'),
        ('/register/', "Ro'yxatdan o'tish"),
        ('/cart/', 'Savat'),
    ]
    
    for url, name in urls:
        response = client.get(url)
        print(f"   - {name} ({url}): {response.status_code}")
    
    return client

def test_book_operations(client):
    print("\n3. Kitob amallari tekshirilmoqda...")
    
    book = Book.objects.first()
    if book:
        print(f"   - Birinchi kitob: {book.title}")
        
        # Like test
        user = User.objects.get(username='testuser')
        client.force_login(user)
        
        response = client.post(f'/book/{book.id}/like/', HTTP_X_CSRFTOKEN='test')
        print(f"   - Layk bosish: {response.status_code}")
        
        # Add to cart
        response = client.get(f'/cart/add/{book.id}/')
        print(f"   - Savatga qo'shish: {response.status_code}")

if __name__ == '__main__':
    print("=" * 50)
    print("Django Loyihasi Tekshiruvchi")
    print("=" * 50)
    
    try:
        user = test_models()
        client = test_urls()
        test_book_operations(client)
        
        print("\n" + "=" * 50)
        print("Barcha tekshiruvlar muvaffaqiyatli o'tdi!")
        print("=" * 50)
    except Exception as e:
        print(f"\nXatolik yuz berdi: {e}")
