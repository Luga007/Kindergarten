from django.urls import path
from .views import (meal_data_page, ingredient_page,
                    delete_meal, delete_ingredient,
                    meal_distribution, meal_ingredient_page, deleteMealIngredients, cook_meal_view, deleteMealDistribution)

urlpatterns = [
    path('mealData/', meal_data_page, name='mealData'),
    path('delete_meal/<int:meal_id>', delete_meal, name='delete_meal'),

    path('ingredientPage/', ingredient_page, name='ingredientPage'),
    path('ingredientDelete/<int:ingredient_id>', delete_ingredient, name='ingredientDelete'),

    path('mealIngredientPage/', meal_ingredient_page, name='mealIngredientPage'),
    path('mealIngredientPage/<int:mealIngredient_id>', deleteMealIngredients, name='deleteMealIngredients'),


    path('cookMealView/', cook_meal_view, name='cookMealView'),

    path('mealDistribution/', meal_distribution, name='mealDistribution'),
    path('mealDistribution/<int:mealdistribution_id>', deleteMealDistribution, name='deleteMealDistribution'),
]