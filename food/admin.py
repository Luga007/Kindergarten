from django.contrib import admin
from .models import Ingredient, MealDistribution, Meal, MealIngredient
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(MealDistribution)
admin.site.register(Meal)
admin.site.register(MealIngredient)
