from django.forms import ModelForm
from .models import Diary


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'text']
