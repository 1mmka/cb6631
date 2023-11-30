from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    
    def __str__(self):
        return self.title