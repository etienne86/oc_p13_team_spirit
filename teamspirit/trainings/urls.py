from django.urls import path
from django.views.generic import TemplateView

# from teamspirit.events import views


app_name = 'trainings'

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="trainings/trainings.html"),
        name="trainings"
    ),
]
