from django.urls import path
from .views import ClinicList, ClinicDetail,ClinicListCreate

urlpatterns = [
    path("", ClinicList.as_view(), name="clinic_list"),
    path("create/",ClinicListCreate.as_view(), name="ClinicListCreate_list"),
    path("<int:pk>/", ClinicDetail.as_view(), name="clinic_detail"),
]