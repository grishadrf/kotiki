from django.shortcuts import render

from products.models import ProductCategory, Product

def index(request):
    context = {
        'title': 'kotiki',
        'is_promotion': False
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - шопимся',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)