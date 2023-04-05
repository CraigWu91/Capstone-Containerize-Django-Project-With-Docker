from django.db import models

# Create your models here.
class Post(models.Model):
# Default behaviour - Django creates primary keys for you
    '''
    Create model with fields title, body, signature and date that represents a blog post

    param: models.Model: Using django built in models module

    return: Title of the blog post

    rtype: string
    '''
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Craig")
    date = models.DateTimeField()
    
def __str__(self):
    return self.title