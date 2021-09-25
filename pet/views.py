from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer


class PetList(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer

