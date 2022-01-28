from django.db import models

# Create your models here.
# tasks/models.py
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
