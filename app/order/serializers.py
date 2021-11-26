from typing import Dict, Any

from rest_framework import serializers

from food.models import Food
from food.serializers import FoodCreateSerializer
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    foods = FoodCreateSerializer(many=True)

    def create(self, validated_data: Dict[Any, Any]) -> Order:
        food_ids = validated_data.pop("foods")
        id_list = [_id['id'] for _id in food_ids]
        foods = Food.objects.filter(id__in=id_list)

        order = Order.objects.create(**validated_data)

        for food in foods:
            order.foods.add(food)

        return order

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['status']
