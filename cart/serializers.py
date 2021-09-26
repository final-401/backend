from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Order,OrderItem
from phonenumber_field.serializerfields import PhoneNumberField
from pet.serializers import SuppliesSerializer
from pet.models import Supplies

class OrderItemserializers(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    product = SuppliesSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Supplies.objects.all(),source='product',write_only=True)
    class Meta:
        model = OrderItem
        fields = "__all__"



class Orderserializers(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    order=OrderItemserializers(many=True,read_only=True)
    
    class Meta:
        model = Order
        fields = "__all__"
