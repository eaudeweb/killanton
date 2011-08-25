from django import forms
from models import Task

class AddForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('finished', 'finished_datetime')
