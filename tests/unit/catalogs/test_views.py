"""Contain the unit tests related to the views in app ``catalogs``."""

from django.test import TestCase
from django.urls import reverse

from teamspirit.users.models import User


class CatalogsViewsTestCase(TestCase):
    """Test the views in the app ``catalogs``."""

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

    def test_catalog_view(self):
        """Unit test - app ``catalogs`` - view ``catalog_view``

        Test the catalog view.
        """
        url = reverse('catalogs:catalog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogs/catalog.html')
