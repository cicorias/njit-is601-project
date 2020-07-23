
from django import forms
from django.forms import models

from survey.models import Question, Survey


#  TODO: remove
class ResponseForm(models.ModelForm):
    class Meta(object):
        model = Survey
        fields = ()
