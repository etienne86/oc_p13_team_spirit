"""Contain the unit tests related to the views in app ``profiles``."""

from django.test import TestCase
from django.urls import reverse

from teamspirit.users.models import User


class ProfilesViewsTestCase(TestCase):
    """Test the views in the app ``profiles``."""

    def setUp(self):
        super().setUp()
        # a user in database
        self.user = User.objects.create_user(
            email="toto@mail.com",
            first_name="Toto",
            password="TopSecret"
        )
        # log this user in
        self.client.login(email="toto@mail.com", password="TopSecret")

    def test_profile_view(self):
        """Unit test - app ``profiles`` - view ``profile_view``

        Test the profile view.
        """
        url = reverse('profiles:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
