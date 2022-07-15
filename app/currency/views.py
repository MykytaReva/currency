from django.http import HttpResponse
from currency.utils import generate


def generator(request):
    result = generate()
    return HttpResponse(result)
