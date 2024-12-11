from django.core.exceptions import ValidationError
from rest_framework import serializers
from users.models import CustomUser, Address, ContactUs
from cloudinary.models import CloudinaryField
from django.contrib.auth.hashers import make_password

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        
    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.country = validated_data.get('country', instance.country)
        instance.building_number = validated_data.get('building_number', instance.building_number)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'phone', 'password', 'confirm_password', 
            'first_name', 'last_name', 'addresses'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def create(self, validated_data):
        addresses_data = self.context.get('addresses', [])
        validated_data.pop('confirm_password', None) 
        user = CustomUser.objects.create_user(**validated_data) 

        # Manejo de direcciones
        for address_data in addresses_data:
            Address.objects.create(user=user, **address_data)

        return user

    def validate(self, data):
        # Validaciones de email y teléfono únicos
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'This email is already registered.'})

        if CustomUser.objects.filter(phone=data['phone']).exists():
            raise serializers.ValidationError({'phone': 'This phone number is already registered.'})
        
        if data['password'] != data.get('confirm_password'):
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        return data

    
class FullUserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone', 'image', 'addresses']

class BasicUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    image = CloudinaryField()
    password = serializers.CharField(required=False, write_only=True)
    confirm_password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'image', 'password', 'confirm_password']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        email = data.get('email')
        phone = data.get('phone')
        username = data.get('username')

        # Validaciones de campos únicos
        if CustomUser.objects.filter(email=email).exists() and email != self.instance.email:
            raise serializers.ValidationError({'email': 'This email is already registered.'})
        
        if CustomUser.objects.filter(phone=phone).exists() and phone != self.instance.phone:
            raise serializers.ValidationError({'phone': 'This phone number is already registered.'})
        
        if CustomUser.objects.filter(username=username).exists() and username != self.instance.username:
            raise serializers.ValidationError({'username': 'This username is already registered.'})

        # Validación de contraseñas
        if password:
            if not confirm_password:
                raise serializers.ValidationError({'confirm_password': 'Please enter the confirm password.'})
            elif password != confirm_password:
                raise serializers.ValidationError({'password': 'Passwords do not match.'})

        return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)

        # Manejo de direcciones eliminado en este serializador
        if password and confirm_password:
            validated_data['password'] = make_password(password)

        return super().update(instance, validated_data)
        
class ContactUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUs
        fields = '__all__'