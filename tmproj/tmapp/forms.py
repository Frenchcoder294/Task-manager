from django import forms
from .models import Task, User
from django.forms import DateTimeInput
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'notes', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 6}),
            'notes': forms.Textarea(attrs={'cols': 60, 'rows': 3}),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

