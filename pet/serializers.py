from rest_framework import serializers
from .models import Pet ,Supplies


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = Pet

class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = Supplies