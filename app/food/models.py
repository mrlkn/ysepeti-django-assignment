from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=127)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

