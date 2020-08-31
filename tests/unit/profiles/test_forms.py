"""Contain the unit tests related to the forms in app ``profiles``."""

from django.test import TestCase

from teamspirit.core.models import Address
from teamspirit.profiles.forms import (
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    UpdatePersonalInfoForm,
    UpdateAddressForm,
)
from teamspirit.profiles.models import Personal
from teamspirit.users.models import User


class ProfilesFormsTestCase(TestCase):
    """Test the forms in the app ``profiles``."""

    def setUp(self):
        super().setUp()
        # a user in database
        self.address = Address.objects.create(
            label_first="1 rue de l'impasse",
            label_second="",
            postal_code="75000",
            city="Paris",
            country="France"
        )
        self.personal = Personal.objects.create(
            phone_number="01 02 03 04 05",
            address=self.address
        )
        self.user = User.objects.create_user(
            email="toto@mail.com",
            password="Password123",
            first_name="Toto",
            last_name="LE RIGOLO",
            personal=self.personal

        )
        # log this user in
        self.client.login(email="toto@mail.com", password="Password123")

    def test_custom_password_change_form_success(self):
        """Unit test - app ``profiles`` - form ``CustomPasswordChangeForm`` #1

        Test the custom password change form with success.
        """
        form_data = {
            'old_password': 'Password123',
            'new_password1': 'Password456',
            'new_password2': 'Password456'
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_password_change_form_failure_wrong_old_password(self):
        """Unit test - app ``profiles`` - form ``CustomPasswordChangeForm`` #2

        Test the custom password change form with failure: wrong old password.
        """
        form_data = {
            'old_password': 'Password000',
            'new_password1': 'Password456',
            'new_password2': 'Password456'
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                'old_password':
                [
                    "Votre ancien mot de passe est incorrect. "
                    "Veuillez le rectifier."
                ]
            }
        )

    def test_custom_password_change_form_failure_différent_new_passwords(self):
        """Unit test - app ``profiles`` - form ``CustomPasswordChangeForm`` #3

        Test the custom password change form with failure:
        different new passwords.
        """
        form_data = {
            'old_password': 'Password123',
            'new_password1': 'Password456',
            'new_password2': 'Password789'
        }
        form = CustomPasswordChangeForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'new_password2': ["Les deux mots de passe ne correspondent pas."]}
        )

    def test_password_reset_form_success(self):
        """Unit test - app ``profiles`` - form ``PasswordResetForm`` #1

        Test the password reset form with success.
        """
        form_data = {
            'email': 'toto@mail.com',
        }
        form = CustomPasswordResetForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_reset_form_failure_wrong_email(self):
        """Unit test - app ``profiles`` - form ``PasswordResetForm`` #2

        Test the password reset form with failure: wrong email.
        """
        form_data = {
            'email': 'foobar',
        }
        form = CustomPasswordResetForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_password_reset_confirm_form_success(self):
        """Unit test - app ``profiles`` - form ``SetPasswordForm`` #1

        Test the password set form with success.
        """
        form_data = {
            'new_password1': 'Password456',
            'new_password2': 'Password456'
        }
        form = CustomSetPasswordForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_reset_confirm_form_failure_two_different_passwords(self):
        """Unit test - app ``profiles`` - form ``SetPasswordForm`` #2

        Test the password set form with failure: two different passwords.
        """
        form_data = {
            'new_password1': 'Password456',
            'new_password2': 'Password789'
        }
        form = CustomSetPasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'new_password2': ["Les deux mots de passe ne correspondent pas."]}
        )

    def test_update_personal_info_form_success(self):
        """Unit test - app ``profiles`` - form ``UpdatePersonalInfoForm`` #1

        Test the personal info update form with success.
        """
        form_data = {
            'first_name': 'Titi',
            'last_name': 'LE RIKIKI'
        }
        form = UpdatePersonalInfoForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(self.user.first_name, "Titi")
        self.assertEqual(self.user.last_name, "LE RIKIKI")

    def test_update_address_form_success(self):
        """Unit test - app ``profiles`` - form ``UpdateAddressForm`` #1

        Test the address update form with success.
        """
        form_data = {
            'label_first': '1 rue du Pont',
            'label_second': '',
            'postal_code': '75000',
            'city': 'Paris',
            'country': 'France'
        }
        form = UpdateAddressForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())
        expected_address = Address.objects.create(
            label_first="1 rue du Pont",
            label_second="",
            postal_code="75000",
            city="Paris",
            country="France"
        )
        self.assertEqual(
            self.user.personal.address.label_first,
            expected_address.label_first
        )
