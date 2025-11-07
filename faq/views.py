from django.shortcuts import render
from .models import Faq

# Create your views here.


def user_faq(request):
    faq = Faq.objects.filter(status="True")

    context = {
        'faq': faq,
    }

    return render(request, 'faq/faq.html', context)
