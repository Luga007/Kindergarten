from django import forms
from . models import Group
from people.models import Caretaker



class GroupForm(forms.ModelForm):
    caretakers = forms.ModelChoiceField(queryset=Caretaker.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Group
        fields = '__all__'