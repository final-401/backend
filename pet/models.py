from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator





class Pet(models.Model):

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pet')
    type=models.CharField(max_length=70,blank=False)
    name_pet = models.CharField(blank=True,max_length=70,null=True)
    description = models.TextField(blank=True,max_length=500,null=True)
    price = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    published = models.DateTimeField(default=timezone.now, blank=True)
    adoption=models.BooleanField(default=False)
    picture = models.ImageField(upload_to='pets', blank=True)

    def __str__(self):  
        return self.name_pet + ' ' + self.type



