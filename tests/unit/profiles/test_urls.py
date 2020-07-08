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
