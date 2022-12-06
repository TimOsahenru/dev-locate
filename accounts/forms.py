from django import forms
from .models import Engineer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class EngineerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = [
            "email",
            "bio",
            "country",
            "avatar",
            "years_of_experience",
            "tech_stack",
        ]
        widgets = {
            "bio": forms.TextInput(attrs={"placeholder": "little about you..."}),
            "tech_stack": forms.TextInput(
                attrs={"placeholder": "stack 1, stack 2, stack 3"}
            ),
        }
