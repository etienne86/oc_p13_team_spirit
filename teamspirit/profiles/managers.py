"""Contain the managers for the models in app ``profiles``."""

from django.db import models

# from django.utils.translation import ugettext_lazy as _


class PersonalManager(models.Manager):
    """Manage the model ``Personal``."""
    pass


class RoleManager(models.Manager):
    """Manage the model ``Role``."""
    pass
