from django import forms
from .models import Kids
from group.models import Group
from kids.models import Parent


class KidsForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    parents = forms.ModelChoiceField(queryset=Parent.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Kids
        fields = '__all__'


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ['address']