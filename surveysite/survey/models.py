from django.db import models

class Survey(models.Model):
  name = models.CharField(max_length = 60)


class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class QuestionType(models.Model):
  name = models.CharField(max_length = 60)

