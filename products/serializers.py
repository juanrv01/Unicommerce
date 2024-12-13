from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.models import AnonymousUser
from .models import Category,Product, Image

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id','image', 'image_url']

    def get_image_url(self, obj):
        return obj.image.url

        
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    images = ImageSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=True)
    is_in_cart = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price','image', 'quantity', 'category', 'images', 'is_in_cart']

    def get_is_in_cart(self, obj):
        user = self.context['request'].user
        if isinstance(user, AnonymousUser):
            return False
        try:
            return user.cart.products.filter(id=obj.id).exists()
        except CustomUser.cart.RelatedObjectDoesNotExist:
            return False
