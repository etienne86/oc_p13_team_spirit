"""Contain the unit tests related to the forms in app ``profiles``."""

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.test import TestCase

from teamspirit.profiles.forms import CustomPasswordChangeForm
from teamspirit.users.models import User


class ProfilesFormsTestCase(TestCase):
    """Test the forms in the app ``profiles``."""

    def setUp(self):
        super().setUp()
        # a user in database
        self.user = User.objects.create_user(
            email="toto@mail.com",
            password="Password123",
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
        form = PasswordResetForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_reset_form_failure_wrong_email(self):
        """Unit test - app ``profiles`` - form ``PasswordResetForm`` #2

        Test the password reset form with failure: wrong email.
        """
        form_data = {
            'email': 'foobar',
        }
        form = PasswordResetForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_password_reset_confirm_form_success(self):
        """Unit test - app ``profiles`` - form ``SetPasswordForm`` #1

        Test the password set form with success.
        """
        form_data = {
            'new_password1': 'Password456',
            'new_password2': 'Password456'
        }
        form = SetPasswordForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_reset_confirm_form_failure_two_different_passwords(self):
        """Unit test - app ``profiles`` - form ``SetPasswordForm`` #2

        Test the password set form with failure: two different passwords.
        """
        form_data = {
            'new_password1': 'Password456',
            'new_password2': 'Password789'
        }
        form = SetPasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'new_password2': ["Les deux mots de passe ne correspondent pas."]}
        )
