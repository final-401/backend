from django.conf import settings
from pet.models import Supplies as Product
from .models import OrderItem, Order
from .serializers import OrderItemserializers,Orderserializers

from rest_framework.permissions import IsAuthenticated


from rest_framework import generics

class CartList(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_class = Orderserializers

class CartDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = Orderserializers




class CartItemList(generics.ListCreateAPIView):

    queryset = OrderItem.objects.all()
    serializer_class  = OrderItemserializers

class CartItemListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = OrderItem.objects.all()
    serializer_class  = OrderItemserializers


