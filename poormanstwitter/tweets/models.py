from django.db import models

# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now=True)
