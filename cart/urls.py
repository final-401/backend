from django.urls import path

from .views import CartList ,CartDetail, CartItemList,CartItemListDetail 
   
app_name = 'shopping_cart'

urlpatterns = [
     path('', CartList.as_view(), name="cartaddlist"),
     path('<int:pk>/', CartDetail.as_view(), name="cartadd_Detail"),
     path('item/', CartItemList.as_view(), name="cartaddlist_Item"),
     path('item/<int:pk>/', CartItemListDetail.as_view(), name="cartadd_Detail_Item"),
]