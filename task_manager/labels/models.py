from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=90, unique=True, verbose_name=_('Name'))

    def __str__(self):
        return self.name
