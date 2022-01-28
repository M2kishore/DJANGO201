from django.db import models

# Create your models here.
# tasks/models.py
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title