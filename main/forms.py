# -*- encoding: utf-8 -*-
from django import forms

class animeGenreForm(forms.Form):
    genero = forms.CharField(label='Género del anime', widget=forms.TextInput, required=True)
    
class animeForm(forms.Form):
    id = forms.CharField(label='ID del anime')