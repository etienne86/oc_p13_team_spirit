from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class CatalogView(TemplateView):

    template_name = "catalogs/catalog.html"


catalog_view = CatalogView.as_view()
catalog_view = login_required(catalog_view)
