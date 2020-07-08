from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class ProfileView(TemplateView):

    template_name = "profiles/profile.html"


profile_view = ProfileView.as_view()
profile_view = login_required(profile_view)
