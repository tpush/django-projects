from django.db import models
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Choice(models.Model):
    author = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option
