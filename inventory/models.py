from django.db import models
from food.models import Ingredient



class Inventory(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    overall_kg = models.IntegerField()
    ordered_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ingredients.name} and quantity"