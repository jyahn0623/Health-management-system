from django import forms
from main.models import Excercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'
    
    