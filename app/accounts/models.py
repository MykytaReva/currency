from django.contrib.auth.models import AbstractUser
from django.db import models

def user_avatar(instance, filename):
    return 'avatars/{0}/{1}'.format(instance.id, filename)

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    avatar = models.FileField(upload_to=user_avatar)

    email = models.EmailField('email address', unique=True)
