from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=29, required=True)
    last_name = forms.CharField(max_length=29, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
