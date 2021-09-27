from django.urls import path
from .views import PetList, PetDetail,SuppliesList,SuppliesDetail


urlpatterns = [
    path('pet/<int:pk>/', PetDetail.as_view(), name='Petdetail'),
    path('pet/', PetList.as_view(), name='Petlist'),
    path('supplies/<int:pk>/', SuppliesDetail.as_view(), name='SuppliesDetail'),
    path('supplies/', SuppliesList.as_view(), name='SuppliesList'),
]
