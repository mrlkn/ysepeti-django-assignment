from django.db import models

from app.food.models import Food
from app.order import choices
from app.restaurant.models import Restaurant
from app.user.models import UserProfile


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
