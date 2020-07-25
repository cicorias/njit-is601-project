from django.db import models

#  hack from
#  https://medium.com/@philamersune/using-postgresql-jsonfield-in-sqlite-95ad4ad2e5f1
from .fields import JSONField


class Survey(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField('Description')
    is_published = models.BooleanField('Users can see it and answer it',
                                       default=False)

    def __str__(self):
        return self.name

#  class QuestionType(models.Model):
#  name = models.CharField(max_length = 60)


class Question(models.Model):
    TEXT = 'text'
    SHORT_TEXT = 'short-text'
    RADIO = 'radio'
    #  SELECT = 'select'

    CHOICES_HELP_TEXT = '''Provide a comma-separated list
    of options for this question.'''

    #  https://github.com/developer11092/django-survey/blob/master/survey/models/question.py
    QUESTION_TYPES = (
        (TEXT, 'Long text (multiple line)'),
        (SHORT_TEXT, 'Short text (one line)'),
        (RADIO, 'Radio Select'),
        #  (SELECT, 'Empty'),
    )

    text = models.CharField('Text', max_length=500)
    survey = models.ForeignKey(Survey,
                               on_delete=models.CASCADE,
                               verbose_name='Survey',
                               related_name='questions')

    choices = models.CharField('Choices', blank=True, null=True,
                               help_text=CHOICES_HELP_TEXT,
                               max_length=100)

    question_type = models.CharField(
                                'Type',
                                max_length=200,
                                choices=QUESTION_TYPES,
                                default=TEXT)

    order = models.IntegerField('Order')

    def __str__(self):
        return 'Survey: {} - Question: {}'.format(self.survey.name, self.text)

    @property
    def button_choices(self):
        return str(self.choices).split(',')

    class Meta(object):
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering = 'survey', 'order'


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    content = JSONField('Response', null=True, blank=True)


class QuestionResponse(models.Model):
    survey_response = models.ForeignKey(
        SurveyResponse, on_delete=models.CASCADE)


# User - do we default to the django user?
# we need anonyminity for the user
