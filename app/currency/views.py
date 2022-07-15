from django.http import HttpResponse
from currency.utils import generate


def printer(request):
    return HttpResponse('Hello World!')


def generator(request):
    result = generate()
    return HttpResponse(result)
