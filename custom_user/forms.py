from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import DateInput, Select
from custom_user.models import CustomUser, Plan
from user_vocabulary.models import Language


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

    field_order = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = user.email
        user.language_preference = 'Ukrainian'
        user.email = self.cleaned_data["email"]
        user.username = ''.join(char for char in user.email if char.isalnum() or char in ['.', '_'])
        user.plan = Plan.objects.get(slug='free')

        if commit:
            user.save()

        return user


class EditUserForm(ModelForm):
    learned_language = ModelChoiceField(queryset=Language.objects.all(), to_field_name='name')
    interface_language = ModelChoiceField(queryset=Language.objects.all(), to_field_name='name')

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'learned_language', 'interface_language']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }

