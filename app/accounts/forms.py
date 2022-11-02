from django import forms
from django.contrib.auth import get_user_model
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from accounts.models import UserAvatar

# def __init__(self, request, *args, **kwargs):
# super().__init__(*args, **kwargs) self.request = request
# def save(self, commit=True): super().save(commit=False)
# self.instance.user = self.request.user
# self.instance.save()
# return self.instance


# def my_view(request):
#     if not request.user.is_authenticated:
#         return request.user.id

class CreateAvatarForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = (
            'u_avatar',
        )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        instance: UserAvatar = super().save(commit=False)
        instance.u_id = self.request.user.id
        instance.save()
        return instance


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password1',
            # 'user_avatar'
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

        self.instance.user = self.request.user

        # if User.objects.last():
        #     u_id = User.objects.last().id + 1
        #     instance.user_avatar_id = u_id
        # else:
        #     u_id = 1
        #     instance.user_avatar_id = u_id

        u_id = self.request.user.id
        if not u_id:
            u_id = 1
        instance.user_avatar_id = u_id

        if commit:
            UserAvatar.objects.create(u_id=u_id, u_avatar='icons/anonymous.png')
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
