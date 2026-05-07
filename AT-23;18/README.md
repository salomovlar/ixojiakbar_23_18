# Kitob Do'koni - Django Loyihasi

## O'rnatish

1. Virtual muhit yarating va faollashtiring:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Kutubxonalarni o'rnating:
```bash
pip install django pillow
```

3. Migratsiyalarni bajaring:
```bash
python manage.py migrate
```

4. Superuser yarating (admin panel uchun):
```bash
python manage.py createsuperuser
```

5. Serverni ishga tushuring:
```bash
python manage.py runserver
```

6. Brauzerda oching: http://127.0.0.1:8000

## Funksional imkoniyatlar

### Foydalanuvchilar uchun:
- Ro'yxatdan o'tish va login qilish
- Kitoblarni ko'rish va qidirish
- Kitoblarga layk bosish
- Savatga kitob qo'shish va boshqarish
- Buyurtma berish (manzil bilan)
- Buyurtmalarni ko'rish va kuzatish

### Admin uchun:
- Admin panel: /admin/
- Kitoblarni qo'shish, tahrirlash va o'chirish
- Buyurtmalarni qabul qilish yoki rad etish
- Foydalanuvchilarni boshqarish

## Loyiha tuzilishi

- `store/` - Asosiy ilova
  - `models.py` - Ma'lumotlar bazasi modellari
  - `views.py` - Ko'rinishlar va funksiyalar
  - `forms.py` - Formalar
  - `urls.py` - URL manzillari
  - `templates/` - HTML shablonlar
- `bookstore/` - Loyiha sozlamalari
- `media/` - Yuklangan rasmlar
- `db.sqlite3` - Ma'lumotlar bazasi

## Foydalanish

1. Admin sifatida kirish: /admin/ yoki /login/
2. Kitoblarni boshqarish: /admin/books/
3. Buyurtmalarni ko'rish: /admin/orders/
4. Foydalanuvchi profili va buyurtmalar: /orders/
