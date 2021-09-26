
from django.db import models
from django.conf import settings

from pet.models import Supplies,Profile



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    # items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class OrderItem(models.Model):
    product = models.OneToOneField(Supplies, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')

    def __str__(self):
        return self.product.product_name
