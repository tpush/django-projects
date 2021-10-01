from django.db import models
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Choice(models.Model):
    option = models.TextField(max_length=100)
    author = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option
