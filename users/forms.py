from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from custom_user.models import CustomUser


class CreateMemberForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

    field_order = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = user.email
        user.email = self.cleaned_data["email"]
        user.username = ''.join(char for char in user.email if char.isalnum() or char in ['.', '_'])
        print(user.username)
        if commit:
            user.save()

        return user


# class EditMemberForm(ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'first_name', 'last_name', 'date_of_birth']

