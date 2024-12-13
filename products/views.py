
from .models import Product
from .serializers import ProductSerializer
from products.pagination import ProductPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer

class CategoryListView(ListAPIView):
    """
    API para listar todas las categorías.
    """
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
   

class ProductListByCategory(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category__id=category_id)

    # Deshabilitar la paginación
    pagination_class = None

    
class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        if search_term:
            return Product.objects.filter(name__icontains=search_term)
        else:
            return Product.objects.all()
        
