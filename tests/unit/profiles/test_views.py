"""Contain the unit tests related to the views in app ``profiles``."""

from unittest.mock import patch

from django.http.request import HttpRequest
from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt

from teamspirit.profiles import forms
from teamspirit.profiles.views import custom_password_change_view, profile_view
from teamspirit.users.models import User


class MockPasswordChangeForm(forms.CustomPasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        self.is_valid = True


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
        # a 'get' request
        self.get_request = HttpRequest()
        self.get_request.method = 'get'
        self.get_request.user = self.user
        # a 'post' request
        self.post_request = HttpRequest()
        self.post_request.method = 'post'
        self.post_request.user = self.user

    def test_profile_view(self):
        """Unit test - app ``profiles`` - view ``profile_view``

        Test the profile view.
        """
        view = profile_view
        template_response = view(self.get_request)
        # render the response content
        template_response.render()
        html = template_response.content.decode('utf8')
        self.assertEqual(template_response.status_code, 200)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Team Spirit - Profil</title>', html)

    @patch(target='forms.CustomPasswordChangeForm', new=MockPasswordChangeForm)
    def test_custom_password_change_view(self):
        """Unit test - app ``profiles`` - view ``custom_password_change_view``

        Test the custom password change view.
        """
        view = custom_password_change_view
        response = csrf_exempt(view)(self.get_request)
        # render the response content
        # response.render()
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn(
            '<title>Team Spirit - Changement de mot de passe</title>',
            html
        )

    # def test_password_changed_view(self):
    #     """Unit test - app ``profiles`` - view ``password_changed_view``

    #     Test the 'password changed' (confirmation) view.
    #     """
    #     url = reverse('profiles:change_password_done')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'profiles/password_changed.html')

    # def test_password_reset_view(self):
    #     """Unit test - app ``profiles`` - view ``custom_password_reset_view``

    #     Test the custom password reset view.
    #     """
    #     url = reverse('profiles:reset_password')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response,
    #         'profiles/reset_password/password_reset.html'
    #     )

    # def test_password_reset_done_view(self):
    #     """Unit test - app ``profiles`` - view ...

    #     [complete view: ``custom_password_reset_done_view``]
    #     Test the custom password reset (done) view.
    #     """
    #     url = reverse('profiles:reset_password_done')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response,
    #         'profiles/reset_password/password_reset_done.html'
    #     )

    # def test_password_reset_confirm_view(self):
    #     """Unit test - app ``profiles`` - view ...

    #     [complete view: ``custom_password_reset_confirm_view``]
    #     Test the custom password reset confirm view.
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

    # def test_password_reset_complete_view(self):
    #     """Unit test - app ``profiles`` - view ...

    #     [complete view: ``custom_password_reset_complete_view``]
    #     Test the custom password reset (complete) view.
    #     """
    #     url = reverse('profiles:reset_password_complete')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response,
    #         'profiles/reset_password/password_reset_complete.html'
    #     )
