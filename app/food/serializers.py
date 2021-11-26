from rest_framework import serializers

from food.models import Food, Category


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ["categories"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FoodCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
