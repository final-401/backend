from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Clinic

class SuppliesModelTests(APITestCase):

    
    def setUp(self):

        self.test_user = get_user_model().objects.create_user(user_name='Anas',password='1234',email='a@a.com',first_name='test',phone='077168528',role='doctor')
        self.test_user.save()

        account_info={
            "email": "a@a.com",
            "password": "1234"}

        response= self.client.post('/api/v1/token/',account_info,format='json')
        token=response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        self.data={
            
            "clinc_name": "Sowr",
            "location": "aaa",
            "starthoure": "02:01:00",
            "endhoure": "14:01:00",
            "phone": "+962777168528",
            "email": "a@ww.com",
            "picture": "11111",
            "user": 1}


    
    
    

    
    def test_create_cinic(self):
         
        url = reverse('ClinicListCreate_list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
        self.assertEqual(Clinic.objects.count(), 1)

    