from currency.models import Rate, ContactUs
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'rate_list.html', context=context)


def contact_us(request):
    context = {
        'contactus_list': ContactUs.objects.all(),
    }

    return render(request, 'contact_us.html', context=context)
