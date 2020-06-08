"""Contain the models related to the app ``profiles``."""


from django.db import models
from django.utils.translation import ugettext_lazy as _

from teamspirit.core.models import Address
from teamspirit.profiles.managers import PersonalManager, RoleManager


class Personal(models.Model):
    """Contain personal information."""

    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First name')
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last name')
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Phone number')
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
    )
    has_private_profile = models.BooleanField(default=False)

    objects = PersonalManager()


class Role(models.Model):
    """Qualify user's role."""

    is_on_board = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    objects = RoleManager()
