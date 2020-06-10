"""Contain the models related to the app ``core``."""


from django.db import models


class Address(models.Model):
    """Contain address fields."""

    label_first = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    label_second = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        max_length=5,
        blank=False,
        null=False
    )
    city = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    country = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )


class Location(models.Model):
    """Name an address."""

    name = models.CharField(
        max_length=100,
        verbose_name="Libellé du lieu",
        unique=True
    )
    address = models.OneToOneField(
        to=Address,
        on_delete=models.CASCADE
    )
