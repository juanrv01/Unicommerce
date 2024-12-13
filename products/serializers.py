from rest_framework import serializers

from users.models import CustomUser
from django.contrib.auth.models import AnonymousUser


from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    is_in_cart = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'category', 'is_in_cart']

    def get_is_in_cart(self, obj):
        user = self.context['request'].user
        if isinstance(user, AnonymousUser):
            return False
        try:
            return user.cart.products.filter(id=obj.id).exists()
        except CustomUser.cart.RelatedObjectDoesNotExist:
            return False
