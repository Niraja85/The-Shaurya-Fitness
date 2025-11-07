from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    messages.success(request, "Thank you for contacting us!")
    return render(request, 'contact/contact.html')
