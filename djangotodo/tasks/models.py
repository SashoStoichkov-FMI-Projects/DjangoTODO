from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_team = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    importance = models.CharField(max_length=255)
    person_responsible = models.CharField(max_length=255)
    due_date = models.DateField()

    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
