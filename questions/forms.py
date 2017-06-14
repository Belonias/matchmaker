from django import forms
from .models import Question

class UserResponseForm(forms.Form):
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
