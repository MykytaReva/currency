from django import forms
from django.contrib.auth import get_user_model
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class MyProfileForm(forms.ModelForm):
    avatar = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'avatar',
        )

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password1',
        )

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords missmatch')

        return cleaned_data

    def save(self, commit=True):
        instance: get_user_model() = super().save(commit=False)
        instance.username = str(uuid.uuid4())
        instance.is_active = False
        instance.set_password(self.cleaned_data['password1'])

        if commit:
            instance.save()

        self._send_activation_email()

        return instance

    def _send_activation_email(self):
        subject = 'Activate your account'
        body = f'''
        Activation link: {settings.HTTP_SCHEMA}://{settings.DOMAIN}{reverse('accounts:user_activate',
                                                                            args=(self.instance.username, ))}
        '''

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [self.instance.email],
            fail_silently=False,
        )
