from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from app.restaurant import serializers
from app.restaurant.models import Restaurant


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestaurantSerializer
    queryset = Restaurant.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
