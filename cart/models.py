
from django.db import models
from django.conf import settings

from pet.models import Supplies


class OrderItem(models.Model):
    product = models.OneToOneField(Supplies, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.product_name



