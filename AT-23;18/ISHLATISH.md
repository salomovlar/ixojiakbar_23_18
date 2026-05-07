# Tezkor ishlatish qo'llanmasi

## Serverni ishga tushirish
```bash
cd "C:\Users\alfatech.uz\Music\AT 23-20"
python manage.py runserver
```

## Sahifalar
- **Bosh sahifa**: http://127.0.0.1:8000/
- **Admin panel**: http://127.0.0.1:8000/admin/
- **Login**: http://127.0.0.1:8000/login/
- **Ro'yxatdan o'tish**: http://127.0.0.1:8000/register/
- **Savat**: http://127.0.0.1:8000/cart/
- **Buyurtmalarim**: http://127.0.0.1:8000/orders/

## Admin ma'lumotlari
- **Username**: admin
- **Password**: admin123

## Asosiy funksiyalar

### Foydalanuvchi uchun:
1. Ro'yxatdan o'tish - username, email, password
2. Login qilish
3. Kitoblarni ko'rish va layk bosish
4. Savatga qo'shish
5. Checkout (manzil kiritish)
6. Buyurtmalarni kuzatish

### Admin uchun:
1. Kitoblarni qo'shish/tahrirlash/o'chirish: /admin/books/
2. Buyurtmalarni ko'rish va statusini o'zgartirish: /admin/orders/
3. Django admin paneli: /admin/

## Kitob qo'shish (admin)
1. /admin/books/ sahifasiga kiring
2. "Yangi kitob qo'shish" tugmasini bosing
3. Ma'lumotlarni to'ldiring (rasm ixtiyoriy)
4. Saqlang

## Buyurtmani boshqarish (admin)
1. /admin/orders/ sahifasiga kiring
2. Buyurtma qabul qilish uchun "Qabul qilish" tugmasi
3. Rad etish uchun "Rad etish" tugmasi
4. Yakunlash uchun "Yakunlash" tugmasi

## Muammolarni hal qilish
- Agar server ishlamasa: `python manage.py runserver` qayta ishga tushiring
- Ma'lumotlar bazasi xatosi: `python manage.py migrate` bajaring
- Rasm yuklanmasa: `media` papkasi mavjudligini tekshiring
