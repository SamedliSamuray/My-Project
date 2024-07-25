from django import forms
from .models import Color

class ColorForm(forms.ModelForm):
    color_code = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Color
        fields = ['clName', 'color_code']


    