# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=30, blank=True)
#     password = models.CharField(max_length=60)
#     email = models.EmailField(max_length=60)

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
    )

    def __str__(self):
        return self.username
