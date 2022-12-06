from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["engineer"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Max 100 char"}),
            "tech_used": forms.TextInput(attrs={"placeholder": "stack 1, stack 2"}),
        }
