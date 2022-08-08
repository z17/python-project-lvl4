from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=90)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reporter_id")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee_id")

    def get_absolute_url(self):
        return "/tasks/%i/" % self.id
