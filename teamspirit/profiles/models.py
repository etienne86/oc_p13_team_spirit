"""Contain the models related to the app ``profiles``."""

from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _

from teamspirit.core.models import Address
from teamspirit.profiles.managers import PersonalManager, RoleManager


class Personal(models.Model):
    """Contain personal information."""

    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Phone number'),
        null=True
    )
    address = models.ForeignKey(
        to=Address,
        on_delete=models.CASCADE,
        null=True
    )
    id_file = models.FileField(null=True, blank=True)
    medical_file = models.FileField(null=True, blank=True)
    has_private_profile = models.BooleanField(default=False)

    objects = PersonalManager()


class Role(models.Model):
    """Qualify user's role."""

    is_member = models.BooleanField(
        default=True,
        verbose_name="Adhérent(e) de l'association"
    )
    is_secretary = models.BooleanField(
        default=False,
        verbose_name="Secrétariat"
    )
    is_treasurer = models.BooleanField(
        default=False,
        verbose_name="Trésorerie"
    )
    is_president = models.BooleanField(
        default=False,
        verbose_name="Présidence"
    )
    is_inactive = models.BooleanField(
        default=False,
        verbose_name="Non adhérent(e)"
    )

    objects = RoleManager()

    def set_as_member(self):
        """Qualify the user as member."""
        with transaction.atomic():
            self.is_member = True
            self.is_secretary = False
            self.is_treasurer = False
            self.is_president = False
            self.is_inactive = False

    def set_as_secretary(self):
        """Qualify the user as secretary."""
        with transaction.atomic():
            self.is_member = False
            self.is_secretary = True
            self.is_treasurer = False
            self.is_president = False
            self.is_inactive = False

    def set_as_treasurer(self):
        """Qualify the user as treasurer."""
        with transaction.atomic():
            self.is_member = False
            self.is_secretary = False
            self.is_treasurer = True
            self.is_president = False
            self.is_inactive = False

    def set_as_president(self):
        """Qualify the user as president."""
        with transaction.atomic():
            self.is_member = False
            self.is_secretary = False
            self.is_treasurer = False
            self.is_president = True
            self.is_inactive = False

    def set_as_inactive(self):
        """Qualify the user as inactive."""
        with transaction.atomic():
            self.is_member = False
            self.is_secretary = False
            self.is_treasurer = False
            self.is_president = False
            self.is_inactive = True
