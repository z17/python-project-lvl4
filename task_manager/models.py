from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=90)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reporter_id")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee_id")
    labels = models.ManyToManyField(Label, through='TaskLabel', through_fields=('task', 'label'))

    def get_absolute_url(self):
        return "/tasks/%i/" % self.id


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
