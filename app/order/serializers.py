from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from food.serializers import FoodCreateSerializer
from order.models import Order
from restaurant.models import Restaurant


class OrderSerializer(serializers.ModelSerializer):
    foods = FoodCreateSerializer(many=True)

    def create(self, validated_data: Dict[Any, Any]) -> Order:
        food_ids = validated_data.pop("foods")
        id_list = [_id['id'] for _id in food_ids]

        restaurant = validated_data.pop("restaurant")
        foods = Restaurant.objects.get(uuid=restaurant.uuid).foods.filter(id__in=id_list)
        if not foods:
            raise ValidationError({'message': 'Invalid food id input for this restaurant'})

        order = Order.objects.create(restaurant_id=restaurant.uuid, **validated_data)

        for food in foods:
            order.foods.add(food)

        return order

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['status']
