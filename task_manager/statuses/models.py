from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=_('Name'))

    def __str__(self):
        return self.name
