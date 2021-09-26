from django.urls import path

from .views import (
    cartaddlist,
    cartadd_Detail,
    cartaddlist_Item,cartadd_Detail_Item
)

app_name = 'shopping_cart'

urlpatterns = [
     path('cartaddlist/', cartaddlist.as_view(), name="cartaddlist"),
     path('cartaddlist/<int:pk>', cartadd_Detail.as_view(), name="cartadd_Detail"),
     path('additem/', cartaddlist_Item.as_view(), name="cartaddlist_Item"),
     path('additem/<int:pk>', cartadd_Detail_Item.as_view(), name="cartadd_Detail_Item"),
]