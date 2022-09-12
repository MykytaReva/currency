from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatar(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    avatar = models.FileField(default='anonymous.png', upload_to=user_avatar, blank=True)
    email = models.EmailField('email address', unique=True)