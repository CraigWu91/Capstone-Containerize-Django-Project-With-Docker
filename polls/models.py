import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

def was_published_recently(self):
    """
    Returns a boolean indicating whether the Question instance was published recently or not.

    return: true if the question was published in the last day, otherwise false
   
    """
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Question(models.Model):
    """
    Returns the object question

    return: string
   
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    """
    Returns the object choice

    return: string
   
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
  
