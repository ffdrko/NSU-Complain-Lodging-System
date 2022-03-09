from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nsu_id = models.CharField(max_length=10, unique=True)
    nsu_card = models.ImageField(upload_to='NSU_ID_CARD/')
    is_student = models.BooleanField(default=False)
    is_systemAdmin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_helpingStaff = models.BooleanField(default=False)
    is_adminEmployee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nsu_id', 'nsu_card']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False
