from django.db import models
from django.contrib.auth.models import (
        BaseUserManager, AbstractBaseUser, PermissionsMixin
    )

# Create your models here.

class CstomUserManager(BaseUserManager):

    def create_superuser(self, name, email, phone_number, password=None, **kwargs):
        if not email:
            raise ValueError('user must have an email address')

        if not name:
            raise ValueError('user must have a name')

        if not phone_number:
            raise ValueError('user must have a phone number')
        
        user = self.model(
                name=name,
                email=self.normalize_email(email),
                phone_number = self.phone_number,
                is_superuser = True,
            )
        user.is_admin = True
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, name, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')

        if not name:
            raise ValueError('user must have a name')

        user = self.model(
                name=name,
                email=self.normalize_email(email)
            )
        user.set_password(password)
        user.save(using = self._db)
        return user

class CustomUser( AbstractBaseUser, PermissionsMixin ):

    name = models.CharField(verbose_name='user name', max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    phone_number = models.BigIntegerField(default='0', verbose_name='phone number')
    objects = CstomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.name

