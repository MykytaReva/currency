from time import time
from currency.models import ResponseLog


def log(self, request):
    start = time()
    response = self.get_response(request)
    end = time()
    timer = end - start
    rlog = ResponseLog.objects.create(
        response_time=timer,
        request_method=request.method,
        query_params=request.GET,
        ip=request.META.get('REMOTE_ADDR'),
        path=request.path,
    )
    rlog.save()
    return response
