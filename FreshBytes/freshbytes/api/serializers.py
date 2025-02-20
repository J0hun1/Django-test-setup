from rest_framework import serializers

from home.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'category_description', 'category_type', 'added_on']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'product_name', 'product_description', 'product_qnty', 'product_type']