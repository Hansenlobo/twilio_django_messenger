from django import forms
from django.forms import ModelForm
from .models import *


class ScoreForm(forms.ModelForm):
    class Meta:
        model=Score
        fields='__all__'