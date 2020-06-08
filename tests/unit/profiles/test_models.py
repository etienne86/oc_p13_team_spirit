"""Contain the unit tests related to the models in app ``profiles``."""


from django.test import TestCase

from teamspirit.core.models import Address
from teamspirit.profiles.models import Personal


class PersonalModelTestsCase(TestCase):
    """Test the model ``Personal``."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.address = Address(
            label_first="1 rue de l'impasse",
            label_second="",
            postal_code=75000,
            city="Paris",
            country="France"
        )
        cls.personal_public = Personal(
            first_name="Foo",
            last_name="Dejoy",
            phone_number="01 02 03 04 05",
            address=cls.address
        )
        cls.personal_public.save()
        cls.personal_private = Personal(
            first_name="Bar",
            last_name="Tabba",
            phone_number="05 04 03 02 01",
            address=cls.address,
            has_private_profile=True
        )
        cls.personal_private.save()

    def test_first_name(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.1

        Test the first name.
        """
        self.assertIsInstance(self.personal_public.first_name, str)
        self.assertEqual(self.personal_public.first_name, "Foo")

    def test_last_name(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.2

        Test the last name.
        """
        self.assertIsInstance(self.personal_public.last_name, str)
        self.assertEqual(self.personal_public.last_name, "Dejoy")

    def test_phone_number(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.3

        Test the phone number.
        """
        self.assertIsInstance(self.personal_public.phone_number, str)
        self.assertEqual(self.personal_public.phone_number, "01 02 03 04 05")

    def test_address(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.4

        Test the address.
        """
        self.assertIsInstance(self.personal_public.address, Address)
        self.assertEqual(self.personal_public.address, self.address)

    def test_has_not_private_profile(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.5

        Test the non-private (i.e. public) profile.
        """
        self.assertIsInstance(self.personal_public.has_private_profile, bool)
        self.assertEqual(self.personal_public.has_private_profile, False)

    def test_has_private_profile(self):
        """Unit test - app ``profiles`` - model ``Personal`` - #1.6

        Test the private profile.
        """
        self.assertIsInstance(self.personal_private.has_private_profile, bool)
        self.assertEqual(self.personal_private.has_private_profile, True)
