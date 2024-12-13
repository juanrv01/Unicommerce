from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
import os


class Category(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=100, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    
    def __str__(self):
        return self.name
