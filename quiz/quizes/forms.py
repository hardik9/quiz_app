from django import forms
from .models import TrueFalseQuestion


class AddTrueFalseForm(forms.ModelForm):
    class Meta:
        model = TrueFalseQuestion
        fields = ['question', 'answer']
    