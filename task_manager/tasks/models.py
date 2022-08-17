from django.db import models

from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=90, verbose_name=_('Name'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('Status'))
    text = models.TextField(verbose_name=_('Description'))
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reporter_id",
        verbose_name=_('Reporter')
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assignee_id",
        blank=True,
        null=True,
        verbose_name=_('Assignee')
    )
    labels = models.ManyToManyField(
        Label,
        through='TaskLabel',
        through_fields=('task', 'label'),
        blank=True,
        verbose_name=_('Labels')
    )

    def get_absolute_url(self):
        return "/tasks/%i/" % self.id


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
