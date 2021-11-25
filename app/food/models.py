from django.db import models


class Category(models.Model):
    id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=127)


class Food(models.Model):
    name = models.CharField(max_length=127)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="categories", blank=True, null=True
    )
