from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _





class Clinic(models.Model):

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clinic')

    clinc_name = models.CharField(blank=True,max_length=70,null=True)
    location = models.TextField(blank=True,max_length=500,null=True)
    starthoure=models.TimeField(help_text="Hour:Minute",blank=True)
    endhoure=models.TimeField(help_text="Hour:Minute",blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    picture = models.ImageField(upload_to='clinc', blank=True)


    def __str__(self):  
        return self.clinc_name + ' -> ' + str(self.user)


