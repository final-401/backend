from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class NewUser(AbstractBaseUser, PermissionsMixin):

    options=(
        ('customer','Customer'),
        ('doctor','Doctor'),
    )
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=70, unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    address = models.TextField(max_length=70, blank=True)
    phone = models.IntegerField(max_length=14, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    role = models.CharField(
        max_length=12, choices=options, default='customer'
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name