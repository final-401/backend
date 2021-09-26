from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


from django.conf import settings
from pet.models import Supplies as Product
from pet.models import Profile
from .extras import generate_order_id
from .models import OrderItem, Order
from .serializers import OrderItemserializers,Orderserializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated


from rest_framework import generics


class cartCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, **kwargs):
        # get the user profile
        user_profile = get_object_or_404(Profile, user=request.user)
        # filter products by id
        product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
        print('productzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        # check if the user already owns this product

        # if product in request.user.profile.ebooks.all():

        #     messages.info(request, 'You already own this ebook')
        #     return redirect(reverse('products:product-list')) 


        # create orderItem of the selected product
        order_item, status = OrderItem.objects.get_or_create(product=product)
        # create order associated with the user
        user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
        user_order.items.add(order_item)
        if status:
            # generate a reference code
            user_order.ref_code = generate_order_id()
            user_order.save()

        # show confirmation message and redirect back to the same page
        messages.info(request, "item added to cart")
        return " ok kkkkkkkkkkkkkkkkkkkkkkkkkkk"



class cartaddlist(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_class = Orderserializers

class cartadd_Detail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = Orderserializers




class cartaddlist_Item(generics.ListCreateAPIView):

    queryset = OrderItem.objects.all()
    serializer_class  = OrderItemserializers

class cartadd_Detail_Item(generics.RetrieveUpdateDestroyAPIView):

    queryset = OrderItem.objects.all()
    serializer_class  = OrderItemserializers


