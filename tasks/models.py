from django.db import models

class Task (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
