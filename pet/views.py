from rest_framework import generics
from .models import Pet,Supplies
from .serializers import PetSerializer,SuppliesSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser


class PetList(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class SuppliesList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Supplies.objects.all()
    serializer_class = SuppliesSerializer


class SuppliesDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)

    queryset = Supplies.objects.all()
    serializer_class = SuppliesSerializer
