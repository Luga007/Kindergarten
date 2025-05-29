from django import forms
from .models import Meal, Ingredient, MealDistribution, MealIngredient
from people.models import Caretaker
from group.models import Group


class MealCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Meal', 'label': 'Meal'}))
    timestamp = forms.CharField(max_length=30,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Timestamp', 'label': 'Timestamo'}))
    estimate_portion = forms.IntegerField(max_value=500,
                                          widget=forms.NumberInput(
                                              attrs={'class': 'form-control', 'placeholder': 'EstimatePortion',
                                                     'label': 'EstimatePortion'}))
    cooked_by = forms.ModelChoiceField(queryset=Caretaker.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'CookedBy'}))
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(MealCreateForm, self).__init__(*args, **kwargs)
        self.fields['ingredients'].queryset = Ingredient.objects.all()

    class Meta:
        model = Meal
        fields = '__all__'


class MealUpdateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class IngredientCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingredient name',
                                                         'label': 'ingredient name'}))
    spoiled_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Spoiled date',
                'type': 'date',
            }
        ),
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MealDistributionCreateForm(forms.ModelForm):
    meal = forms.ModelChoiceField(queryset=Meal.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Meal'}))
    served_by = forms.ModelChoiceField(queryset=Caretaker.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'ServeBy'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'group'}))

    DATE_TIME_CHOICE = (
        (1, 'breakfast'),
        (2, 'lunch'),
        (3, 'dinner'),
    )
    served_date = forms.ChoiceField(
        choices=DATE_TIME_CHOICE,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Date'})
    )
    served_day = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Spoiled date',
                'type': 'date',
            }
        ),
        input_formats=['%Y-%m-%d'],
    )
    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes'}))


    class Meta:
        model = MealDistribution
        fields = '__all__'




class MealIngredientForm(forms.ModelForm):
    meal = forms.ModelChoiceField(queryset=Meal.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Meal'}))
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingredient'}))
    kilo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kilo'}))

    class Meta:
        model = MealIngredient
        fields = '__all__'
