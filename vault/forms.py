from django import forms
from django.forms.widgets import HiddenInput
from . import models

class JoinForm(forms.Form):
   group_id = forms.CharField(required=True, min_length=7, max_length=7)
   name = forms.CharField(max_length=200, required=True)
   image = forms.CharField(widget=forms.Textarea)

class CreateForm(forms.Form):
    meeting_url = forms.URLField(
       required=True)

    def __init__(self, *args, **kwargs):
        members = int(kwargs['member_count'])
        kwargs.pop('member_count')
        super(CreateForm, self).__init__(*args, **kwargs)
        if members == 0: 
           members +=1

        for i in range(members):
            self.fields[f'name_{i}'] = forms.CharField(max_length = 200, label = 'Name', required=True)
            self.fields[f'image_{i}'] = forms.ImageField(label = 'Image', required=True)

class CreateCountForm(forms.Form):
   count = forms.IntegerField(min_value=1, required=True)

