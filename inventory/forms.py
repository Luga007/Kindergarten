from django import forms
from food.models import Ingredient
from .models import Ingredient, Inventory


class InventoryForm(forms.ModelForm):
    ingredients = forms.ModelChoiceField(queryset=Ingredient.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Meal'}))
    overall_kg = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'kg'}))
    ordered_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Spoiled date',
                'type': 'date',
            }
        ),
        input_formats=['%Y-%m-%d'])

    class Meta:
        model = Inventory
        exclude = ('is_active',)