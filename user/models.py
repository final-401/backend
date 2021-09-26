from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name,phone, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name,phone, password, **other_fields)

    def create_user(self, email, user_name, first_name,phone, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name,phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    options=(
        ('customer','Customer'),
        ('doctor','Doctor'),
    )
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=70, unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    address = models.TextField(max_length=230, blank=True)
    # phone = models.IntegerField(max_length=14, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=1000,blank=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    role = models.CharField(
        max_length=12, choices=options, default='customer'
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','phone']

    def __str__(self):
        return self.user_name

