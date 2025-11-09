from django.shortcuts import redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Newsletter


# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type a valid email address")
            return redirect(('home'))
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = Newsletter()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        messages.success(request, "Thank you for subscribing!")
        return redirect(request.META.get("HTTP_REFERER", "/"))







