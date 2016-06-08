from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    decription = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
