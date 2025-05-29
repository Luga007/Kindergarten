from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from address.models import Address


class CareTakerManger(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Caretakers must have an email address')
        caretaker = self.model(email=self.normalize_email(email), first_name=first_name, is_active=True)
        caretaker.set_password(password)
        caretaker.save(using=self._db)
        return caretaker

    def create_superuser(self, email, first_name, password=None):
        caretaker = self.create_user(email, first_name, password)
        caretaker.is_admin = True
        caretaker.is_superuser = True
        caretaker.is_staff = True
        caretaker.is_active = True
        caretaker.save(using=self._db)
        return caretaker


class Roles(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    CARETAKER = 'caretaker', 'Caretaker'
    CHIEF = 'chief', 'Chief'

class Caretaker(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=75, unique=True)
    role = models.CharField(max_length=20, choices=Roles.choices)
    number = models.CharField(max_length=25, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    joined_date = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CareTakerManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



