from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from  .models import OrderItem,Order
from  pet.models import Supplies



class APITest(APITestCase):
    
    def setUp(self):

        self.test_user = get_user_model().objects.create_user(user_name='Anas',password='1234',email='a@a.com',first_name='test',phone='077168528')
        self.test_user.save()

        self.test_order=Order.objects.create(ref_code="ABCD1234FEG56",owner=self.test_user)
        self.test_order.save()

        self.test_supply=Supplies.objects.create(type="cat food",product_name="mesho",price=1,)
        self.test_supply.save()





        account_info={
            "email": "a@a.com",
            "password": "1234"}

        response= self.client.post('/api/v1/token/',account_info,format='json')
        token=response.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


 

    def test_list(self):
        url=['/api/v1/cart/','/api/v1/cart/item/']

        
        response = self.client.get(url[0])
        response2 = self.client.get(url[1])
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


    

    def test_create_order(self):
     
        url ='/api/v1/cart/'
        data={
      "owner": self.test_user.id,
      "ref_code":"123321Aa",

    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
        self.assertEqual(Order.objects.count(), 2)


    def test_create_order(self):
     
        url ='/api/v1/cart/item/'
        data={
      "order": self.test_order.id,
      "product_id":self.test_order.id,

    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
