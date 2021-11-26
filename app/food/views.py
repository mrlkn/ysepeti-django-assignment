from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from food import serializers
from food.models import Food, Category


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FoodSerializer
    queryset = Food.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
