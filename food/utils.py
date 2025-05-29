from inventory.models import Inventory
from django.db import transaction
from attendance.models import Attendance
from .models import MealDistribution, MealIngredient


def cook_meal_with_inventory(meal_distribution_id):
    try:
        distribution = MealDistribution.objects.get(id=meal_distribution_id)
    except MealDistribution.DoesNotExist:
        return "Error: MealDistribution not found"

    served_date = distribution.served_day.date()
    meal = distribution.meal
    group = distribution.group

    try:
        attendance = Attendance.objects.filter(group=group, date=served_date).first()
    except Attendance.DoesNotExist:
        return f"No data on group attendance {group.group_name} on {served_date}"

    if not attendance:
        return f"No attendance record found for group {group.group_name} on {served_date}"
    kids_count = attendance.kids_arrived

    if kids_count == 0:
        return "Not a single child came - no need to cook."

    if kids_count == 0:
        return "Not a single child came - no need to cook."

    meal_ingredients = MealIngredient.objects.filter(meal=meal)
    not_enough = []


    for mi in meal_ingredients:
        total_required = mi.kilo * kids_count
        inventories = Inventory.objects.filter(
            ingredients=mi.ingredient, is_active=True
        ).order_by("ordered_date")

        total_available = sum(inv.overall_kg for inv in inventories)

        if total_available < total_required:
            not_enough.append(
                f"{mi.ingredient.name}: need {total_required:.2f} kg, have {total_available:.2f} kg"
            )

    if not_enough:
        return " Not enough ingredients:\n" + "\n".join(not_enough)


    with transaction.atomic():
        for mi in meal_ingredients:
            total_required = mi.kilo * kids_count
            inventories = Inventory.objects.filter(
                ingredients=mi.ingredient, is_active=True
            ).order_by("ordered_date")

            for inv in inventories:
                if total_required <= 0:
                    break
                if inv.overall_kg >= total_required:
                    inv.overall_kg -= total_required
                    inv.save()
                    total_required = 0
                else:
                    total_required -= inv.overall_kg
                    inv.overall_kg = 0
                    inv.save()

    return f" {meal.name}'prepared for {kids_count} kids from the group {group.group_name}!"
