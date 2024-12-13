from django.urls import path, include
from .views import  ProductListByCategory, ProductList,CategoryListView

urlpatterns = [
    path('category/<int:category_id>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('search/', ProductList.as_view(), name='product-list-search'),
    path('categories/', CategoryListView.as_view(), name='category-list'),

]
