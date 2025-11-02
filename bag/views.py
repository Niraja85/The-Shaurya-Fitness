from django.shortcuts import render


# Create your views here.
""" A view to return the index page"""


def view_bag(request):
    return render(request, 'bag/bag.html')
