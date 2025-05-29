from django.db import models
from people.models import Caretaker
from collections import defaultdict
from datetime import timezone, timedelta, datetime, date
from group.models import Group



def default_time():
    return date.today() + timedelta(days=30)



class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    spoiled_date = models.DateField(default=default_time)

    def __str__(self):
        return self.name



class Meal(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    estimate_portion = models.FloatField(null=False)
    cooked_by = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    required_grams = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class MealDistribution(models.Model):
    DATE_TIME_CHOICE = (
        (1, 'breakfast'),
        (2, 'lunch'),
        (3, 'dinner'),
    )
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    served_by = models.ForeignKey(Caretaker, on_delete=models.CASCADE)
    served_date = models.IntegerField(choices=DATE_TIME_CHOICE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    served_day = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.served_date}"



class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    kilo = models.FloatField()

    def __str__(self):
        return f"{self.meal}, {self.ingredient}. kilo = {self.kilo}"






# class MonthlyReport(models.Model):
#     month = models.DateField()
#     total_meals_served = models.IntegerField()
#     total_ingredients_used = models.JSONField()
#     generated_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Report for {self.month.strftime('%B %Y')}"
