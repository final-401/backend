from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from  .models import NewUser



class APITest(APITestCase):
    
    def setUp(self):

        self.test_user = get_user_model().objects.create_user(user_name='Anas',password='1234',email='a@a.com',first_name='test',phone='077168528')
        self.test_user.save()

        account_info={
            "email": "a@a.com",
            "password": "1234"}

        response= self.client.post('/api/v1/token/',account_info,format='json')
        token=response.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


 

    def test_list(self):

        response = self.client.get('/api/v1/user/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


    def test_exist_user(self):
        assert  self.test_user.user_name=="Anas"
        assert  self.test_user.first_name=="test"


        


    def test_create_user(self):
     
        url ='/api/v1/user/create/'
        data={
      "email": "a@aa.com",
      "password":"123321Aa",
      "user_name": "anass",
      "phone": "0777168524",
      "first_name": "Anas",
      "role": "doctor",
      "last_name": "Abu",
      "address": "Amman 100",
      "picture":"imageurl"

    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
        self.assertEqual(NewUser.objects.count(), 2)
