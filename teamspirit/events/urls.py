from django.urls import path
from django.views.generic import TemplateView

# from teamspirit.events import views


app_name = 'events'

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="events/events.html"),
        name="events"
    ),
]
