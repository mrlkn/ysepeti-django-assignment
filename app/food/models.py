from django.db import models


class Category(models.Model):
    # Fields
    name = models.CharField(max_length=127)

    # Functions
    def __str__(self):
        return self.name


class Food(models.Model):
    # Fields
    name = models.CharField(max_length=127)
    categories = models.ManyToManyField(Category)

    # Functions
    def __str__(self):
        return self.name
