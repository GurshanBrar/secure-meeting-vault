from django import forms
from . import models


class CreateForm(forms.Form):
    meeting_url = forms.URLField(
        verbose_name='Meeting Link', blank=False, help_text="Enter the meeting link")
    name = forms.CharField(max_length=200, blank=False)
    image = forms.ImageField()
