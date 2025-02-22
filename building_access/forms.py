from django import forms

from .models import Building


class LetMeInForm(forms.Form):
    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop("queryset", None)
        super().__init__(*args, **kwargs)
        self.fields["building"].queryset = queryset

    building = forms.ModelChoiceField(queryset=Building.objects.all())
