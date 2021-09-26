from django.urls import path
from .views import CustomUserCreate , UserList

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/', UserList.as_view(), name="user_user"),

 
]