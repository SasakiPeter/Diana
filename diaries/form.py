from django import forms
from django.forms import ModelForm

from .models import Diary


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'text', 'pub_date']


class DiarySearchForm(forms.Form):
    title = forms.CharField(label="", max_length=200, required=False)
