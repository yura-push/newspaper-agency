from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience",)


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("years_of_experience",)


class NewspaperCreationForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
