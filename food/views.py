from django.http import JsonResponse

from .models import Meal, Ingredient, MealDistribution, MealIngredient
from django.shortcuts import render
from .forms import MealCreateForm, IngredientCreateForm, MealUpdateForm, IngredientUpdateForm, MealIngredientForm, MealDistributionCreateForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .utils import cook_meal_with_inventory
from django.contrib import messages
from .permissions import can_access_admin, can_access_chief, can_access_caretaker

@login_required(login_url='login')
def meal_data_page(request):
    meals = Meal.objects.all()
    form = None
    create_form = MealUpdateForm()

    edit_meal_id = request.GET.get('edit_meal_id')

    if not can_access_caretaker and can_access_chief:
        return render(request, 'caretaker.html')
    if request.method == 'POST':
        if edit_meal_id:
            meal_to_edit = get_object_or_404(Meal, id=edit_meal_id)
            form = MealUpdateForm(request.POST, instance=meal_to_edit)
            if form.is_valid():
                form.save()
                return redirect('mealData')
        else:

            create_form = MealUpdateForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('mealData')
    else:

        if edit_meal_id:
            try:
                meal_to_edit = Meal.objects.get(id=edit_meal_id)
                form = MealUpdateForm(instance=meal_to_edit)
            except Meal.DoesNotExist:
                form = None

    context = {
        'meals': meals,
        'form': form,
        'create_form': create_form,
        'edit_meal_id': edit_meal_id,
        'user_role': request.user.role,
    }
    return render(request, 'meal.html', context)


def delete_meal(request, meal_id):
    user = get_object_or_404(Meal, id=meal_id)
    user.delete()
    return redirect('mealData')


# def ingredient_page(request):
#     ingredients = Ingredient.objects.all()
#     ctx = {'ingredients': ingredients}
#     return render(request, 'ingredient.html', ctx)


@login_required(login_url='login')
def ingredient_page(request):
    ingredient = Ingredient.objects.all()
    form = None
    create_form = IngredientCreateForm()

    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    edit_ingredient_id = request.GET.get('edit_ingredient_id')

    if request.method == 'POST':
        if edit_ingredient_id:
            ingredient_to_edit = get_object_or_404(Ingredient, id=edit_ingredient_id)
            form = IngredientCreateForm(request.POST, instance=ingredient_to_edit)
            if form.is_valid():
                form.save()
                return redirect('ingredientPage')
        else:
            create_form = IngredientCreateForm(request.POST)
            print(create_form)
            print(create_form.is_valid())
            print(create_form.errors)
            if create_form.is_valid():
                create_form.save()
                return redirect('ingredientPage')
    else:
        if edit_ingredient_id:
            try:
                ingredient_to_edit = Ingredient.objects.get(id=edit_ingredient_id)
                form = IngredientCreateForm(instance=ingredient_to_edit)
            except Ingredient.DoesNotExist:
                form = None
        else:
            form = None

    context = {
        'ingredients': ingredient,
        'form': form,
        'create_form': create_form,
        'edit_ingredient_id': edit_ingredient_id,
        'user_role': request.user.role,
    }
    return render(request, 'ingredient.html', context)


def delete_ingredient(request, ingredient_id):
    user = get_object_or_404(Ingredient, id=ingredient_id)
    user.delete()
    return redirect('ingredientPage')


@login_required(login_url='login')
def meal_ingredient_page(request):
    mealIngredients = MealIngredient.objects.all()
    form = None
    create_form = MealIngredientForm()

    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    edit_mealIngredients_id = request.GET.get('edit_mealIngredients_id')

    if request.method == 'POST':
        if edit_mealIngredients_id:
            mealIngredient_to_edit = get_object_or_404(MealIngredient, id=edit_mealIngredients_id)
            form = MealIngredientForm(request.POST, instance=mealIngredient_to_edit)
            if form.is_valid():
                form.save()
                return redirect('mealIngredientPage')
        else:

            create_form = MealIngredientForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('mealIngredientPage')
    else:

        if edit_mealIngredients_id:
            try:
                meal_to_edit = MealIngredient.objects.get(id=edit_mealIngredients_id)
                form = MealIngredientForm(instance=meal_to_edit)
            except MealIngredient.DoesNotExist:
                form = None



    context = {
        'mealIngredients': mealIngredients,
        'form': form,
        'create_form': create_form,
        'edit_mealIngredients_id': edit_mealIngredients_id,
        'user_role': request.user.role,
    }
    return render(request, 'meal_ingredient.html', context)





def deleteMealIngredients(request, mealIngredient_id):
    mealIngredient_id = get_object_or_404(MealIngredient, id=mealIngredient_id)
    mealIngredient_id.delete()
    return redirect('mealIngredientPage')


def meal_distribution(request):
    mealDistribution = MealDistribution.objects.all()
    form = None
    create_form = MealDistributionCreateForm()
    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    edit_mealDistribution_id = request.GET.get('edit_mealDistribution_id')

    if request.method == 'POST':
        if edit_mealDistribution_id:
            mealDistribution_to_edit = get_object_or_404(MealDistribution, id=edit_mealDistribution_id)
            form = MealDistributionCreateForm(request.POST, instance=mealDistribution_to_edit)
            if form.is_valid():
                form.save()
                return redirect('mealDistribution')

        else:

            create_form = MealDistributionCreateForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('mealDistribution')
    else:

        if edit_mealDistribution_id:
            try:
                meal_to_edit = MealDistribution.objects.get(id=edit_mealDistribution_id)
                form = MealDistributionCreateForm(instance=meal_to_edit)
            except MealDistribution.DoesNotExist:
                form = None

    context = {
        'mealDistributions': mealDistribution,
        'form': form,
        'create_form': create_form,
        'edit_mealDistribution_id': edit_mealDistribution_id,
        'user_role': request.user.role,
    }
    return render(request, 'MealDistribution.html', context)


def deleteMealDistribution(request, mealdistribution_id):
    meal_dis = get_object_or_404(MealDistribution, id=mealdistribution_id)
    meal_dis.delete()
    return redirect('mealDistribution')



def cook_meal_view(request):
    distributions = MealDistribution.objects.select_related('meal', 'group')

    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    if request.method == 'POST':
        dist_id = request.POST.get('distribution_id')
        result = cook_meal_with_inventory(dist_id)
        messages.info(request, result)
        return redirect('cookMealView')

    ctx = {
        'distributions': distributions,
        'user_role': request.user.role,
    }

    return render(request, 'cook_meals.html', ctx)
