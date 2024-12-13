from django.contrib import admin
from products.models import Product, Category

from django.utils.html import mark_safe



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','price','quantity',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)