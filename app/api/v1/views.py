from rest_framework import generics

from currency.models import Rate, Source, ContactUs
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from api.v1.serializer import RateSerializer, SourceSerializer, ContactUsSerializer

from api.v1.pagination import RatePagination

from api.v1.filters import RateFilter

from api.v1.throttles import AnonCurrencyThrottle


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter
    )
    ordering_field = ['id', 'buy', 'sale']
    throttle_classes = [AnonCurrencyThrottle]


class SourceView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
