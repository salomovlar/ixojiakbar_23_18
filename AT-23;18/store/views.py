from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import Book, BookLike, Order, OrderItem, Cart, CartItem, UserProfile
from .forms import RegisterForm, OrderForm, BookForm
import json

def index(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    liked = False
    if request.user.is_authenticated:
        liked = BookLike.objects.filter(book=book, user=request.user).exists()
    return render(request, 'store/book_detail.html', {'book': book, 'liked': liked})

@login_required
def like_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    like, created = BookLike.objects.get_or_create(book=book, user=request.user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': book.likes_count()})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{book.title} savatga qo'shildi")
    return redirect('cart')

@login_required
def cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.total_price()
    return render(request, 'store/cart.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Mahsulot savatdan o'chirildi")
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.warning(request, "Savat bo'sh")
        return redirect('cart')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price()
            order.save()

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=item.book.price
                )

            cart.items.all().delete()
            messages.success(request, "Buyurtma muvaffaqiyatli rasmiylashtirildi")
            return redirect('orders')
    else:
        profile = getattr(request.user, 'profile', None)
        initial = {
            'full_name': request.user.get_full_name() or request.user.username,
            'address': profile.address if profile else '',
            'phone': profile.phone if profile else '',
        }
        form = OrderForm(initial=initial)

    return render(request, 'store/checkout.html', {'form': form, 'cart': cart})

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': orders})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            address = form.cleaned_data.get('address', '')
            phone = form.cleaned_data.get('phone', '')
            UserProfile.objects.create(user=user, address=address, phone=phone)
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz")
            return redirect('index')
        else:
            messages.error(request, "Login yoki parol noto'g'ri")
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz")
    return redirect('index')

@staff_member_required
def admin_books(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'store/admin/books.html', {'books': books})

@staff_member_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Kitob muvaffaqiyatli qo'shildi")
            return redirect('admin_books')
    else:
        form = BookForm()
    return render(request, 'store/admin/book_form.html', {'form': form, 'action': 'Qo\'shish'})

@staff_member_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Kitob muvaffaqiyatli yangilandi")
            return redirect('admin_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'store/admin/book_form.html', {'form': form, 'action': 'Tahrirlash', 'book': book})

@staff_member_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Kitob o'chirildi")
        return redirect('admin_books')
    return render(request, 'store/admin/delete_book.html', {'book': book})

@staff_member_required
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'store/admin/orders.html', {'orders': orders})

@staff_member_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['accepted', 'rejected', 'completed']:
            order.status = status
            order.save()
            messages.success(request, f"Buyurtma holati yangilandi")
    return redirect('admin_orders')
