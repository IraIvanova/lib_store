from django import forms
from django.forms import ModelForm


class SearchBookForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
