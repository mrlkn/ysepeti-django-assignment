import uuid as uuid
from django.db import models

from app.food.models import Food, Category


class Restaurant(models.Model):
    # Fields
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64)

    categories = models.ManyToManyField(Category)
    foods = models.ManyToManyField(Food)

    # Functions
    def __str__(self):
        return self.name
