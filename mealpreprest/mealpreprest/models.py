from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    serving_size = models.IntegerField()
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    unit_cost = models.FloatField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # one to many ingredients?
    # one to many steps?
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class RecipeStep(models.Model):
    recipe = models.ForeignKey('mealpreprest.Recipe',  on_delete=models.CASCADE)
    description = models.CharField(max_length=50)


# ReceiptIngredient table(model)
