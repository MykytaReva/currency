from django import forms
from currency.models import Rate, ContactUs, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'base_currency_type',
            'currency_type',
            'sale',
            'buy',
            'source',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            # 'email_from',
            'email_to',
            'subject',
            'message',
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'url',
            'name',

        )
