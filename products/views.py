from rest_framework import viewsets, decorators, response
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para permitir crear, listar, actualizar y eliminar productos.
    Los administradores pueden crear, modificar y eliminar productos.
    Los usuarios pueden consultar la lista de productos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser] if viewsets.ModelViewSet.action in ['create', 'update', 'partial_update', 'destroy'] else [AllowAny]

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        if search_term:
            return Product.objects.filter(name__icontains=search_term)
        return super().get_queryset()

    @decorators.action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def by_category(self, request, *args, **kwargs):
        """ 
        Endpoint para filtrar productos por ID de la categoría 
        Ejemplo: /api/products/by_category/?category_id=1 
        """
        category_id = request.query_params.get('category_id')
        if category_id:
            products = Product.objects.filter(category__id=category_id)
            page = self.paginate_queryset(products)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(products, many=True)
            return response.Response(serializer.data)
        return response.Response({'detail': 'No se proporcionó category_id'}, status=400)
