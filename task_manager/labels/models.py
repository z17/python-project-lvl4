from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name
