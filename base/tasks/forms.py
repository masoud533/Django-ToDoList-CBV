from django import forms
from .models import Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'New task...',
                'autocomplete': 'off'
            })
        }