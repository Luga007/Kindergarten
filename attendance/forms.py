from django import forms
from .models import Attendance
from group.models import Group


class AttendanceForm(forms.ModelForm):
    date = forms.DateField( widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Spoiled date',
                'type': 'date',
            }
        ),
        input_formats=['%Y-%m-%d'])
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'groups'}))
    kids_arrived = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'kids arrived'}))

    class Meta:
        model = Attendance
        fields = '__all__'