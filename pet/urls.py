from django.urls import path
from .views import PetList, PetDetail


urlpatterns = [
    path('<int:pk>/', PetDetail.as_view(), name='Petdetail'),
    path('', PetList.as_view(), name='Petlist'),
]