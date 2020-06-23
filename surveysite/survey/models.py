from django.db import models

class Survey(models.Model):
  name = models.CharField(max_length = 60)

class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class QuestionOrder(models.Model):
  pass

class SurveyResponse(models.Model):
  pass

class QuestionResponse(models.Model):
  pass

class QuestionType(models.Model):
  name = models.CharField(max_length = 60)

# User - do we default to the django user?
# we need anonyminity for the user

