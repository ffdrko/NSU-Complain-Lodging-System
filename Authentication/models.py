from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200, default='admin')
    phone = models.CharField(max_length=11, unique=True)
    nsu_id = models.CharField(max_length=10, unique=True)
    nsu_card = models.ImageField(upload_to='NSU_ID_CARD/')
    picture = models.ImageField(upload_to='dp/', default='dp/default.png', null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_systemAdmin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_helpingStaff = models.BooleanField(default=False)
    is_adminEmployee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'nsu_id', 'nsu_card']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False


class Student(models.Model):
    DEPARTMENT = (
        ('Not Specified', 'Not Specified'),
        ('Accounting and Finance', 'Accounting and Finance'),
        ('Economics', 'Economics'),
        ('Management', 'Management'),
        ('Marketing and International Business', 'Marketing and International Business'),
        ('Architecture', 'Architecture'),
        ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
        ('Electrical and Computer Engineering', 'Electrical and Computer Engineering'),
        ('Mathematics and Physics', 'Mathematics and Physics'),
        ('English and Modern Languages', 'English and Modern Languages'),
        ('Political Science and Sociology', 'Political Science and Sociology'),
        ('Law', 'Law'),
        ('History and Philosophy', 'History and Philosophy'),
        ('Biochemistry and Microbiology', 'Biochemistry and Microbiology'),
        ('Environmental Science and Management', 'Environmental Science and Management'),
        ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'),
        ('Public Health', 'Public Health'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=DEPARTMENT, default='Not Specified', null=True, blank=True)
    program = models.CharField(max_length=100, null=True, blank=True)


class Faculty(models.Model):
    DEPARTMENT = (
        ('Not Specified', 'Not Specified'),
        ('Accounting and Finance', 'Accounting and Finance'),
        ('Economics', 'Economics'),
        ('Management', 'Management'),
        ('Marketing and International Business', 'Marketing and International Business'),
        ('Architecture', 'Architecture'),
        ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
        ('Electrical and Computer Engineering', 'Electrical and Computer Engineering'),
        ('Mathematics and Physics', 'Mathematics and Physics'),
        ('English and Modern Languages', 'English and Modern Languages'),
        ('Political Science and Sociology', 'Political Science and Sociology'),
        ('Law', 'Law'),
        ('History and Philosophy', 'History and Philosophy'),
        ('Biochemistry and Microbiology', 'Biochemistry and Microbiology'),
        ('Environmental Science and Management', 'Environmental Science and Management'),
        ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'),
        ('Public Health', 'Public Health'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=DEPARTMENT, default='Not Specified', null=True, blank=True)
    is_chairman = models.BooleanField(default=False)


class AdminEmployee(models.Model):
    OFFICE = (
        ('Not Specified', 'Not Specified'),
        ("Registrar's Office", "Registrar's Office"),
        ("Proctor's Office", "Proctor's Office"),
        ('Office of External Affairs', 'Office of External Affairs'),
        ('Office of Graduate Studies', 'Office of Graduate Studies'),
        ('Office of Student Affairs', 'Office of Student Affairs'),
        ('Financial Aid Office', 'Financial Aid Office'),
        ('NSU Startups Next (NSUSN)', 'NSU Startups Next (NSUSN)'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    office = models.CharField(max_length=100, choices=OFFICE, default='Not Specified', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
