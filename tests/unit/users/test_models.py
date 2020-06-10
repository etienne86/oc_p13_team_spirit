"""Contain the unit tests related to the models in app ``users``."""

from django.contrib.auth.hashers import check_password
from django.test import TestCase

from teamspirit.users.models import User


class UserModelTestsCase(TestCase):
    """Test the model ``User``."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.toto = User.objects.create_user(
            email="toto@mail.com",
            password="Password123"
        )
        cls.super_toto = User.objects.create_superuser(
            email="super_toto@mail.com",
            password="Password456"
        )

    def test_create_user(self):
        """Unit test - app ``users`` - model ``User`` #1

        Test the user creation.
        """
        self.assertIsInstance(self.toto, User)
        self.assertEqual(self.toto.email, "toto@mail.com")

    def test_create_superuser(self):
        """Unit test - app ``users`` - model ``User`` #2

        Test the superuser creation.
        """
        self.assertIsInstance(self.super_toto, User)
        self.assertEqual(self.super_toto.email, "super_toto@mail.com")

    def test_user_is_active(self):
        """Unit test - app ``users`` - model ``User`` #3

        Test that the user is active.
        """
        self.assertIsInstance(self.toto.is_active, bool)
        self.assertTrue(self.toto.is_active)

    def test_superuser_is_active(self):
        """Unit test - app ``users`` - model ``User`` #4

        Test that the superuser is active.
        """
        self.assertIsInstance(self.super_toto.is_active, bool)
        self.assertTrue(self.super_toto.is_active)

    def test_user_is_not_superuser(self):
        """Unit test - app ``users`` - model ``User`` #5

        Test that the user is not superuser.
        """
        self.assertIsInstance(self.toto.is_superuser, bool)
        self.assertFalse(self.toto.is_superuser)

    def test_superuser_is_superuser(self):
        """Unit test - app ``users`` - model ``User`` #6

        Test that the superuser is (really) superuser.
        """
        self.assertIsInstance(self.super_toto.is_superuser, bool)
        self.assertTrue(self.super_toto.is_superuser)

    def test_user_is_not_staff(self):
        """Unit test - app ``users`` - model ``User`` #7

        Test that the user is not staff.
        """
        self.assertIsInstance(self.toto.is_staff, bool)
        self.assertFalse(self.toto.is_staff)

    def test_superuser_is_staff(self):
        """Unit test - app ``users`` - model ``User`` #8

        Test that the superuser is staff.
        """
        self.assertIsInstance(self.super_toto.is_staff, bool)
        self.assertTrue(self.super_toto.is_staff)

    def test_user_is_not_admin(self):
        """Unit test - app ``users`` - model ``User`` #9

        Test that the user is not admin.
        """
        self.assertIsInstance(self.toto.is_admin, bool)
        self.assertFalse(self.toto.is_admin)

    def test_superuser_is_admin(self):
        """Unit test - app ``users`` - model ``User`` #10

        Test that the superuser is admin.
        """
        self.assertIsInstance(self.super_toto.is_admin, bool)
        self.assertTrue(self.super_toto.is_admin)

    def test_user_has_right_password(self):
        """Unit test - app ``users`` - model ``User`` #11

        Test that the user has the right password.
        """
        self.assertTrue(check_password("Password123", self.toto.password))

    def test_superuser_has_right_password(self):
        """Unit test - app ``users`` - model ``User`` #12

        Test that the superuser has the right password.
        """
        self.assertTrue(
            check_password("Password456", self.super_toto.password)
        )
