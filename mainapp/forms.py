from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = ['name', 'phone', 'email']

