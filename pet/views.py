from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer
from .permissions import IsOwnerOrReadOnly

class PetList(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
