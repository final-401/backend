from rest_framework import serializers
from .models import Pet ,Supplies
from user.serializers import UserSerializer
from user.models import NewUser

class PetSerializer(serializers.ModelSerializer):

    # pet=UserSerializer(many=True,read_only=True)
    user =UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=NewUser.objects.all(),source='user',write_only=True)


    class Meta:
        fields ='__all__'
        model = Pet

class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        fields =['id','type','product_name','description','price','quantity','published','picture']
        model = Supplies