from django import forms
from django.forms import ModelForm
from .models import UserVocabulary


class SearchWordForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))


class WordForm(ModelForm):
    class Meta:
        model = UserVocabulary
        fields = ["examples"]

    # translation = forms.CharField()
    examples = forms.CharField(required=False, widget=forms.Textarea)

