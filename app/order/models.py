from django.db import models

from food.models import Food
from order import choices
from restaurant.models import Restaurant
from user.models import UserProfile


class Order(models.Model):
    # Fields
    status = models.CharField(
        max_length=3,
        default=choices.PENDING,
        choices=choices.STATUSES
    )

    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    foods = models.ManyToManyField(Food)
