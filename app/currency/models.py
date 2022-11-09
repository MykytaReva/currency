from datetime import datetime

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
    created = models.DateTimeField(default=datetime.utcnow)

    class Meta:
        verbose_name_plural = "Rate"


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=60, default=settings.EMAIL_HOST_USER)
    email_to = models.EmailField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=7000)
    sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ContactUs"


def bank_avatar(instance, filename):
    return 'bank_avatar/{0}/{1}'.format(instance.name, filename)


class Source(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=256)
    code_name = models.CharField(max_length=20, unique=True)
    bank_avatar = models.FileField(blank=True, upload_to=bank_avatar)

    class Meta:
        verbose_name_plural = "Source"


class ResponseLog(models.Model):
    response_time = models.FloatField()
    request_method = models.CharField(max_length=600)
    query_params = models.CharField(max_length=600)
    ip = models.CharField(max_length=600)
    path = models.CharField(max_length=600)

    class Meta:
        verbose_name_plural = "ResponseLog"
