from rest_framework import generics

from currency.models import Rate, Source, ContactUs
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from api.v1.serializer import RateSerializer, SourceSerializer, ContactUsSerializer

from api.v1.pagination import RatePagination

from api.v1.filters import RateFilter, ContactUsFilter, SourceFilter


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
    filterset_class = SourceFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter
    )
    ordering_field = ['id', 'name']
    throttle_classes = [AnonCurrencyThrottle]


class ContactUsView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filterset_class = ContactUsFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter
    )
    search_fields = ['subject', 'email_to', 'message', ]
    ordering_field = ['id', 'sent']
    throttle_classes = [AnonCurrencyThrottle]
