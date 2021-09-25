from django.urls import path
from .views import ClinicList, ClinicDetail

urlpatterns = [
    path("", ClinicList.as_view(), name="clinic_list"),
    path("<int:pk>/", ClinicDetail.as_view(), name="clinic_detail"),
]