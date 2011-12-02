# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50, required=True, label='Recherche',
        error_messages={'required': 'Il faut rechercher quelque chose',
                        'min_length': 'Minimal length : 2 chars',
                        'max_length': 'Maximal length : 50 chars'})
    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get("name")
        return cleaned_data

