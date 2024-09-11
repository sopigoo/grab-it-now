from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Siti Shofi Nadhifa',
        'npm': '2306152172',
        'class': 'PBP D',

        'products': [
            {
                'name': 'Binder',
                'price': 35000,
                'description': 'Binder yang stylish untuk menyimpan dokumenmu.',
                'stock': 2,
                'category': 'Stationery',
                'rating': 4.8,
            },
            {
                'name': 'Pen Set',
                'price': 15000,
                'description': '5 pcs pulpen warna.',
                'stock': 10,
                'category': 'Stationery',
                'rating': 4.5,
            },
            {
                'name': 'Notebook',
                'price': 25000,
                'description': 'Notebook hardcare dengan isi 100 lembar.',
                'stock': 5,
                'category': 'Stationery',
                'rating': 4.9,
            }
        ]
    }

    return render(request, "main.html", context)