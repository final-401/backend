from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Clinic
# from .permissions import IsOwnerOrReadOnly
from .serializers import ClinicSerializer


class ClinicList(ListCreateAPIView):
    queryset = Clinic.objects.all()
    # print(queryset)
    serializer_class = ClinicSerializer


class ClinicDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Clinic.objects.all()
    # serializer_class = ClinicSerializer
