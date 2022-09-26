from rest_framework.serializers import ModelSerializer

from currency.models import Rate, Source, ContactUs
from django.core.mail import send_mail
from django.conf import settings


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'currency_type',
            'base_currency_type',
            'created',
            'source'
        )
        # extra_kwargs = {
        #     'sale': {'read_only': True},
        #     'buy': {'read_only': True},
        # }


class SourceSerializer(ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'url',
            'name',
            'bank_avatar'
        )


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'email_to',
            'subject',
            'message',
            'sent'
        )

    def create(self, validated_data):
        subject = validated_data.get('subject')
        message = validated_data.get('message')
        email_to = validated_data.get('email_to')
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email_to],
            fail_silently=False,
        )
        return ContactUs(**validated_data)
