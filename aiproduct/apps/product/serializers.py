from rest_framework import serializers
from .models import Product, ProductClick, UserUtmParameter, Category


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'url',
            'image_url',
            'description',
            'category_name',
            'category_id',
            'created_at',
            'updated_at'
        ]


class AiProductClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClick
        fields = ['uid', 'click_source', 'product']


class UserUtmParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUtmParameter
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'color']