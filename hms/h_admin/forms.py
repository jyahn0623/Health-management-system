from django import forms
from main.models import *

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = '__all__'

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'
    
class TodoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'
        widgets = {
            'tdl_date' : forms.TextInput(attrs={'placeholder' : 'yyyy-mm-dd'})
        }
    
    
class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = '__all__'

    
    
    
     
    