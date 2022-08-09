from currency.utils import log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith(('/admin/', '/silk')):
            response = self.get_response(request)
            return response

        else:
            response = log(self, request)
            return response
