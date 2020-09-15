"""Contain the managers for the models in app ``profiles``."""

import imp
from django.db import models

from teamspirit.users.models import User


class PersonalManager(models.Manager):
    """Manage the model ``Personal``."""
    pass


class RoleManager(models.Manager):
    """Manage the model ``Role``."""
    pass


def rename_id_file(instance, file_name):
    user = User.objects.get(personal=instance.id)
    return f"pieces_identite/{user.last_name}_{user.first_name}/{file_name}"
    # user = "moi meme"
    # zero = user.split(" ")[0]
    # one = user.split(" ")[1]
    # return f"pieces_identite/{zero}_{one}/{file_name}"

def rename_medical_file(instance, file_name):
    user = User.objects.get(personal=instance.id)
    return f"certificats_licences/{user.last_name}_{user.first_name}/{file_name}"
    # user = "moi meme"
    # zero = user.split(" ")[0]
    # one = user.split(" ")[1]
    # return f"certificats_licences/{zero}_{one}/{file_name}"
