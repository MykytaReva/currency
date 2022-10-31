from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatar(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.u_id, filename)
# format(instance.user_id
# return f'avatar/{uuid.uuid4()}_{filename}'

# class User(AbstractUser):
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     avatar = models.FileField(upload_to=user_avatar, blank=True)
#     email = models.EmailField('email address', unique=True)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    user_avatar = models.ForeignKey(
        'accounts.UserAvatar',
        db_column="Avatar",
        on_delete=models.CASCADE,
        null=True
    )
    email = models.EmailField('email address', unique=True)

    # def get_avatar(self):


class UserAvatar(models.Model):
    u_id = models.IntegerField()
    # u_id = models.ForeignKey(
    #     'accounts.User',
    #     on_delete=models.CASCADE
    # )
    u_avatar = models.FileField(upload_to=user_avatar)
