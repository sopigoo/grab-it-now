from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'binder',
        'price': 'Rp. 35.000',
        'description': 'deskripsi produk',
        'stock': '2',
        'category': 'stationary',
        'rating': '4.8'
    }

    return render(request, "main.html", context)