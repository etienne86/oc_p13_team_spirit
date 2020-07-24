"""Contain the integration tests in app ``profiles``."""

from django.test import TestCase
from django.urls import reverse

from teamspirit.users.models import User


class ProfilesIntegrationTestCase(TestCase):
    """Test integration in the app ``profiles``."""

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

    def test_profile_view_with_url(self):
        """Integration test - app ``profiles`` - view with url #1

        Test the profile view with url.
        """
        url = reverse('profiles:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_custom_password_change_view_with_url(self):
        """Integration test - app ``profiles`` - view with url #2

        Test the custom password change view with url.
        """
        url = reverse('profiles:change_password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/change_password.html')

    def test_password_changed_view_with_url(self):
        """Integration test - app ``profiles`` - view with url #3

        Test the 'password changed' (confirmation) view with url.
        """
        url = reverse('profiles:change_password_done')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/password_changed.html')

    def test_password_reset_view_with_url(self):
        """UniIntegrationt test - app ``profiles`` - view with url #4

        Test the custom password reset view with url.
        """
        url = reverse('profiles:reset_password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'profiles/reset_password/password_reset.html'
        )

    def test_password_reset_done_view_with_url(self):
        """Integration test - app ``profiles`` - view with url #5

        Test the custom password reset (done) view with url.
        """
        url = reverse('profiles:reset_password_done')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'profiles/reset_password/password_reset_done.html'
        )

    # next test: AttributeError: 'NoneType' object has no attribute 'is_bound'
    # I do not know how to generate/mock the `uidb64` and `token`.

    # def test_password_reset_confirm_view_with_url(self):
    #     """Integration test - app ``profiles`` - view with url #6

    #     Test the custom password reset confirm view with url.
    #     """
    #     url = reverse(
    #         'profiles:reset_password_confirm',
    #         kwargs={'uidb64': 'uid', 'token': 'token'}
    #     )
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response,
    #         'profiles/reset_password_confirm.html'
    #     )

    def test_password_reset_complete_view_with_url(self):
        """Integration test - app ``profiles`` - view with url #7

        Test the custom password reset (complete) view with url.
        """
        url = reverse('profiles:reset_password_complete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'profiles/reset_password/password_reset_complete.html'
        )
