from django import forms
from .models import JsonData


class FileForm(forms.ModelForm):
    class Meta:
        model = JsonData
        fields = ['file']
