"""Contain the unit tests related to the urls in app ``profiles``."""

from django.test import TestCase
from django.urls import reverse


class ProfilesUrlsTestCase(TestCase):
    """Test the urls in the app ``profiles``."""

    def test_profile_url(self):
        """Unit test - app ``profiles`` - url ``profile/``

        Test the profile url.
        """
        url = reverse('profiles:profile')
        self.assertEqual(url, '/profile/')

    def test_custom_password_change_url(self):
        """Unit test - app ``profiles`` - url ``profile/change_password/``

        Test the custom password change url.
        """
        url = reverse('profiles:change_password')
        self.assertEqual(url, '/profile/change_password/')

    def test_password_changed_url(self):
        """Unit test - app ``profiles`` - url ``profile/change_password/done/``

        Test the 'password changed' (confirmation) url.
        """
        url = reverse('profiles:change_password_done')
        self.assertEqual(url, '/profile/change_password/done/')
