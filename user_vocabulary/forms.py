from django import forms


class SearchWordForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
