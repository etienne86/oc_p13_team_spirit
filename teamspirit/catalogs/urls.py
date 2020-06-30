from django.urls import path
from django.views.generic import TemplateView

# from teamspirit.catalogs import views


app_name = 'catalogs'

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="catalogs/catalog.html"),
        name="catalog"
    ),
]
