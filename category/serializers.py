from rest_framework import serializers 
from .models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ('slug', 'name')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'