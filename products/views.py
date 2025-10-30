from django.shortcuts import render
from .models import Product

# Create your views here.
""" A view to show all products, including sorting and search queries """

products = Product.objects.all()

context = {
    'products': products,
}


def all_products(request):
    return render(request, 'products/products.html', context)
