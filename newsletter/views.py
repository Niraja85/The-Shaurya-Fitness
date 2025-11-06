from django.shortcuts import render
from .models import Newsletter


# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)




