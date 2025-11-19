from django.shortcuts import render
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


# Create your views here.
def newsletter_subscribe(request):
    form = NewsletterForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             'Your Email already exists in our database',
                             "alert alert-warning alert-dismissable")
        else:
            instance.save()
            messages.success(request,
                             'Thank You for subscribing!!',
                             extra_tags='newsletter')

    context = {
        'form': form,
        }
    template = 'newsletter/subscribe.html'

    return render(request, template, context)
