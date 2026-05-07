import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from store.models import Book

def add_sample_data():
    # Create sample books
    books_data = [
        {
            'title': 'O\'tkan kunlar',
            'author': 'Abdulla Qodiriy',
            'description': 'Oʻzbek adabiyotining durdona asari. Roman oʻzbek xalqi hayotining turli qirralarini, ijtimoiy illatlarni, odamlar oʻrtasidagi munosabatlarni teran ochib beradi.',
            'price': 45000,
            'stock': 10
        },
        {
            'title': 'Mehrobdan chayon',
            'author': 'Abdulla Qodiriy',
            'description': 'Abdulla Qodiriyning yana bir mashhur asari. Asarda diniy xurofotlar, noraso tushunchalar tanqid qilinadi.',
            'price': 40000,
            'stock': 15
        },
        {
            'title': 'Ikki eshik orasi',
            'author': 'Abdulla Qahhor',
            'description': 'Hikoyalar toʻplami. Kundalik hayotdagi kichik voqealar orqali katta falsafiy maʼno ochib beriladi.',
            'price': 35000,
            'stock': 8
        },
        {
            'title': 'Kecha va kunduz',
            'author': 'Oybek',
            'description': 'Oʻzbek adabiyotida birinchi katta romanlardan biri. Asar inqilobiy oʻzgarishlar davri hayoti aks ettirilgan.',
            'price': 50000,
            'stock': 12
        },
        {
            'title': 'Navoiy',
            'author': 'Oybek',
            'description': 'Alisher Navoiy hayoti va ijodi haqidagi tarixiy roman. Buyuk shoirning tarjimai holi badiiy asarda aks etgan.',
            'price': 55000,
            'stock': 6
        },
    ]

    for book_data in books_data:
        Book.objects.create(**book_data)
        print(f"Added book: {book_data['title']}")

    print("\nSample data added successfully!")

if __name__ == '__main__':
    import django
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
    django.setup()
    add_sample_data()
