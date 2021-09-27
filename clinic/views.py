    from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView
)
from .models import Clinic
from .permissions import IsOwnerOrReadOnly ,IsDoctorOrReadOnly
from .serializers import ClinicSerializer


class ClinicList(ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicListCreate(ListCreateAPIView):
    permission_classes = (IsDoctorOrReadOnly,)
    queryset = Clinic.objects.all()
    # print(queryset)
    serializer_class = ClinicSerializer






class ClinicDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
