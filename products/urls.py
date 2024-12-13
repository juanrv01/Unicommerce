from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Creamos el router e incluimos el ViewSet de Product
router = DefaultRouter()
router.register(r'', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),  # Incluir todas las rutas generadas automáticamente
]
