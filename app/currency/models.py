from django.db import models
from currency.model_choices import CurrencyType
from django.conf import settings


class Rate(models.Model):
    base_currency_type = models.CharField(
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.CURRENCY_TYPE_UAH
    )
    currency_type = models.CharField(
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.CURRENCY_TYPE_USD
    )
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=60, default=settings.EMAIL_HOST_USER)
    email_to = models.EmailField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=7000)
    sent = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=256)


class ResponseLog(models.Model):
    response_time = models.FloatField()
    request_method = models.CharField(max_length=4)
    query_params = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    path = models.CharField(max_length=122)
