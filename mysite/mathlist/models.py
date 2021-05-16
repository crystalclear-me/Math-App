import datetime as dt

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_level = models.CharField(max_length=200, default="")

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - dt.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    selection = models.IntegerField(default=0)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
