from django.db.models.signals import post_migrate
from django.dispatch import receiver

from people.models import Caretaker


from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Ingredient, Meal, MealIngredient, Caretaker

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'food':
        caretaker = Caretaker.objects.first()
        if caretaker is None:
            caretaker = Caretaker.objects.create(first_name='Default Caretaker')


        rice, _ = Ingredient.objects.get_or_create(name='rice')
        meat, _ = Ingredient.objects.get_or_create(name='meat')
        oil, _ = Ingredient.objects.get_or_create(name='butter')
        potato, _ = Ingredient.objects.get_or_create(name='potato')
        carrot, _ = Ingredient.objects.get_or_create(name='carrot')
        onion, _ = Ingredient.objects.get_or_create(name='onion')
        egg, _ = Ingredient.objects.get_or_create(name='egg')
        flour, _ = Ingredient.objects.get_or_create(name='flour')
        milk, _ = Ingredient.objects.get_or_create(name='milk')


        plov, _ = Meal.objects.get_or_create(name='plov', defaults={
            'estimate_portion': 1.0,
            'cooked_by': caretaker
        })
        MealIngredient.objects.get_or_create(meal=plov, ingredient=rice, kilo=0.2)
        MealIngredient.objects.get_or_create(meal=plov, ingredient=meat, kilo=0.3)
        MealIngredient.objects.get_or_create(meal=plov, ingredient=oil, kilo=0.1)
        MealIngredient.objects.get_or_create(meal=plov, ingredient=carrot, kilo=0.05)
        MealIngredient.objects.get_or_create(meal=plov, ingredient=onion, kilo=0.03)


        puree, _ = Meal.objects.get_or_create(name='potatoes pure with cutlet', defaults={
            'estimate_portion': 1.0,
            'cooked_by': caretaker
        })
        MealIngredient.objects.get_or_create(meal=puree, ingredient=potato, kilo=0.25)
        MealIngredient.objects.get_or_create(meal=puree, ingredient=meat, kilo=0.2)
        MealIngredient.objects.get_or_create(meal=puree, ingredient=oil, kilo=0.05)
        MealIngredient.objects.get_or_create(meal=puree, ingredient=onion, kilo=0.02)


        pancakes, _ = Meal.objects.get_or_create(name='Blini', defaults={
            'estimate_portion': 1.0,
            'cooked_by': caretaker
        })
        MealIngredient.objects.get_or_create(meal=pancakes, ingredient=flour, kilo=0.2)
        MealIngredient.objects.get_or_create(meal=pancakes, ingredient=milk, kilo=0.3)
        MealIngredient.objects.get_or_create(meal=pancakes, ingredient=egg, kilo=0.1)
        MealIngredient.objects.get_or_create(meal=pancakes, ingredient=oil, kilo=0.05)

