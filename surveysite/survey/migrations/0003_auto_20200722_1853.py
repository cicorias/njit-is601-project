# Generated by Django 3.0.6 on 2020-07-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200722_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.CharField(blank=True, help_text="The choices field is only used if the question type\n    if the question type is 'radio' or 'select' provide a comma-separated list\n    of options for this question .", max_length=500, null=True, verbose_name='Choices'),
        ),
    ]