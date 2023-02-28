from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

<<<<<<< HEAD
=======

class Board(models.Model):
    title =  models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    #users_allow = models.ManyToManyField(User)

    def __str__(slef):
        return slef.title


class Quest(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    state = models.BooleanField(default=False)
    body = models.TextField(null=True, blank=True)	
    create = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(slef):
        return slef.title


class ChildQuest(models.Model):
    title = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)

    def __str__(slef):
        return slef.title

    




class Meta:
    ordering = ['state']
>>>>>>> b8fbabf (add models to api and admin)
