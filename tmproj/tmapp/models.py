from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField(null = True)
    timestamp = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    checked = models.BooleanField(default=False)

    def __str__(self):
        return ', '.join(self.tag.names())

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return ', '.join(self.username.names())