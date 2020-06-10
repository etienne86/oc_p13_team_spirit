"""Contain the models related to the app ``trainings``."""


from django.db import models

from teamspirit.core.models import Location
from teamspirit.profiles.models import Personal
from teamspirit.trainings.managers import TrainingManager


class Training(models.Model):
    """Define a training session."""

    is_weekly = models.BooleanField(
        verbose_name="Entraînement hebdomadaire",
        default="False"
    )
    date = models.CharField(
        max_length=10
    )
    day = models.CharField(
        max_length=10
    )
    time = models.CharField(
        max_length=5
    )
    trainer = models.ForeignKey(
        to=Personal,
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE
    )
    content = models.CharField(
        max_length=100
    )
    note = models.CharField(
        max_length=1000
    )

    objects = TrainingManager()
