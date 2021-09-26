from rest_framework import serializers
from user.models import NewUser
from phonenumber_field.serializerfields import PhoneNumberField

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.


    
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    role=serializers.CharField(required=True)
    first_name=serializers.CharField(required=True)
    phone=PhoneNumberField(required=True)
    
    last_name=serializers.CharField()
    address=serializers.CharField()
    about=serializers.CharField()
    picture=serializers.CharField()
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password','phone','first_name','role','last_name','address','about','picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    # pet=OrderItemserializers(many=True,read_only=True)

    class Meta:
        fields =['id','user_name','first_name','last_name']
        model = NewUser