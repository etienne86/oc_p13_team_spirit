"""
This module contains the unit tests related to
the models in app ``users``.
"""

from django.test import TestCase

from teamspirit.users.models import User


def create_user_toto(email="toto@mail.com"):
    return User.objects.create_user(email=email)


def create_superuser_toto(email="super_toto@mail.com"):
    return User.objects.create_superuser(email=email)


class UserModelTestsCase(TestCase):
    """Test the model ``User``."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.toto = create_user_toto()
        cls.super_toto = create_superuser_toto()

    def test_create_user(self):
        """Unit test - app ``users`` - #1

        Test the user creation.
        """
        self.assertTrue(isinstance(self.toto, User))
        self.assertEqual(self.toto.email, "toto@mail.com")

    def test_create_superuser(self):
        """Unit test - app ``users`` - #2

        Test the superuser creation.
        """
        self.assertTrue(isinstance(self.super_toto, User))
        self.assertEqual(self.super_toto.email, "super_toto@mail.com")

    def test_user_is_active(self):
        """Unit test - app ``users`` - #3

        Test that the user is active.
        """
        self.assertTrue(self.toto.is_active)

    def test_superuser_is_active(self):
        """Unit test - app ``users`` - #4

        Test that the superuser is active.
        """
        self.assertTrue(self.super_toto.is_active)

    def test_user_is_not_superuser(self):
        """Unit test - app ``users`` - #5

        Test that the user is not superuser.
        """
        self.assertFalse(self.toto.is_superuser)

    def test_superuser_is_superuser(self):
        """Unit test - app ``users`` - #6

        Test that the superuser is (really) superuser.
        """
        self.assertTrue(self.super_toto.is_superuser)

    def test_user_is_not_staff(self):
        """Unit test - app ``users`` - #7

        Test that the user is not staff.
        """
        self.assertFalse(self.toto.is_staff)

    def test_superuser_is_staff(self):
        """Unit test - app ``users`` - #8

        Test that the superuser is staff.
        """
        self.assertTrue(self.super_toto.is_staff)

    def test_user_is_not_admin(self):
        """Unit test - app ``users`` - #9

        Test that the user is not admin.
        """
        self.assertFalse(self.toto.is_admin)

    def test_superuser_is_admin(self):
        """Unit test - app ``users`` - #10

        Test that the superuser is admin.
        """
        self.assertTrue(self.super_toto.is_admin)
