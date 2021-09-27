from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from  .models import Pet,Supplies



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

        self.data = {
            "user_id":self.test_user.id,
            "type": "Dog",
            "name_pet": "FOFO",
            "description": "aa",
            "price": 20.0,
            "published": "2021-09-27T17:46:45.612630Z",
            "adoption": False,
            "picture": "111"}

        self.test_pet = Pet.objects.create(
            user_id = self.test_user.id,
            type = 'cat',
            name_pet="me",
            description="test",
            price=10.0,
            adoption=False,
            published="2021-09-27T18:37:47.162347Z",
            picture= "111"
        )
        self.test_pet.save()

 

    def test_list(self):

        response = self.client.get(reverse('Petlist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


    def test_create_user(self):
        assert  self.test_user.user_name=="Anas"
        assert  self.test_user.first_name=="test"


        


    def test_create_pet(self):
     
        url = reverse('Petlist')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, self.test_user.id)
        self.assertEqual(Pet.objects.count(), 2)


    def test_update_pet(self):
        url = reverse('Petdetail',args=[self.test_pet.id])
        data = {
            "user_id": 1,
            "type": "DogGGGGG",
            "name_pet": "FOFO",
            "description": "aa",
            "price": 20.0,
            "published": "2021-09-27T18:37:47.162347Z",
            "picture": "111"}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, url)





# class SuppliesModelTests(APITestCase):

    
#     def setUp(self):
#         self.test_user = get_user_model().objects.create_user(user_name='Anas',password='1234',email='a@a.com',first_name='test',phone='077168528',role='doctor')
#         self.test_user.save()
#         account_info={
#             "email": "a@a.com",
#             "password": "1234"}
#         response= self.client.post('/api/v1/token/',account_info,format='json')
#         token=response.json()['access']
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

#         self.test_Supply=Supplies.objects.create(
#             type="food",
#             product_name="JoMo Dog Food",
#             description="super healthy Dog Food ",
#             price="10"

#         )
#         self.test_Supply.save()

#     def test_create(self):
       
#         url=reverse('SuppliesList')
#         data={
#         "type": "Dog",
#         "product_name": "Nice Food",
#         "description": "",
#         "price": 0.0,
#         "quantity": 1,
#         "published": "2021-09-27T19:54:41.232001Z",
#         "picture": ""
#     }
       

#         response = self.client.post(url, data, format='json')
#         print('***'*10)
#         print(response)
#         print('***'*10)
        



