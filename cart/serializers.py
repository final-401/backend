from rest_framework import serializers
from .models import Order,OrderItem
from phonenumber_field.serializerfields import PhoneNumberField

class OrderItemserializers(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    
    class Meta:
        model = OrderItem
        fields = "__all__"



class Orderserializers(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    order=OrderItemserializers()
    
    class Meta:
        model = Order
        fields = "__all__"
