"""Contain the unit tests related to the views in app ``events``."""

from django.test import TestCase
from django.urls import reverse

from teamspirit.users.models import User


class EventsViewsTestCase(TestCase):
    """Test the views in the app ``events``."""

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

    def test_events_view(self):
        """Unit test - app ``events`` - view ``events_view``

        Test the events view.
        """
        url = reverse('events:events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
