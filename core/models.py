from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date_created = models.DateTimeField()
    done = models.BooleanField(default=False)