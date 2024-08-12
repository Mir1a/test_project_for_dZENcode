from django.contrib import auth
from django.db import models

from . import managers


class User(auth.models.AbstractBaseUser,
           auth.models.PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    homepage = models.URLField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    objects = managers.CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.homepage:
            self.homepage = f'/users/{self.name}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
