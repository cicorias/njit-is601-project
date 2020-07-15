from django.contrib import admin

# Register your models here.

from .models import Survey, Question, QuestionType

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(QuestionType)