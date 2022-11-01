from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatar(instance, filename):
    return 'avatar/{0}/{1}'.format(instance.u_id, filename)

# def get_user_id():
#     return UserAvatar.objects.get_or_create(u_id=request.user.id)[0]


class User(AbstractUser):
    #
    # def __init__(self, request, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.request = request
    #
    # def get_user_id(self):
    #     return UserAvatar.objects.get_or_create(u_id=self.request.user.id)[0]
    #
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
    # user_avatar = models.ForeignKey(
    #     'accounts.UserAvatar',
    #     db_column="Avatar",
    #     on_delete=models.SET(get_user_id),
    #     null=True
    # )
    # email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    user_avatar = models.ForeignKey(
        'accounts.UserAvatar',
        db_column="Avatar",
        on_delete=models.CASCADE,
        null=True
    )
    email = models.EmailField('email address', unique=True)


class UserAvatar(models.Model):
    u_id = models.IntegerField()
    u_avatar = models.FileField(upload_to=user_avatar, default='icons/anonymous.png')

    # u_id = models.ForeignKey(
    #     'accounts.User',
    #     on_delete=models.CASCADE
    # )
