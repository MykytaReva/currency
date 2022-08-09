from time import time
from currency.models import ResponseLog


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def log(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        timer = end - start
        ResponseLog.objects.create(
            response_time=timer,
            request_method=request.method,
            query_params=request.GET,
            ip=request.META.get('REMOTE_ADDR'),
            path=request.path,
        )
        return response

    def __call__(self, request):

        if request.path.startswith(('/admin/', '/silk')):
            response = self.get_response(request)
            return response

        else:
            response = SimpleMiddleware.log(self, request)
            return response
