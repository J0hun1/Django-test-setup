# Create your views here.
from rest_framework import viewsets

from.serializers import CategorySerializer, ProductSerializer
from home.models import Category, Product

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # SELECT * FROM Category
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() # SELECT * FROM Product
    serializer_class = ProductSerializer