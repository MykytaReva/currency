from django.http import HttpResponse
from currency.utils import generate


def generator(request):
    result = generate()
    x = 11
    print(11)



    return HttpResponse(result)
