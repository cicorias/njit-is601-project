from django.contrib import admin

# Register your models here.

from .models import Survey, Question


class QuestionInLine(admin.StackedInline):
    model = Question
    save_on_top = True
    extra = 1


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ['name', 'description', 'is_published']
    inlines = [QuestionInLine, ]


# admin.site.register(Survey, SurveyAdmin)
# admin.site.register(Question)
