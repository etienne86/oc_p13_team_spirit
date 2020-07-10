from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView

from teamspirit.profiles.forms import CustomPasswordChangeForm


class ProfileView(TemplateView):

    template_name = "profiles/profile.html"


profile_view = ProfileView.as_view()
profile_view = login_required(profile_view)


class CustomPasswordChangeView(PasswordChangeView):

    template_name = 'profiles/change_password.html'
    success_url = 'done'
    form_class = CustomPasswordChangeForm


custom_password_change_view = CustomPasswordChangeView.as_view()
custom_password_change_view = login_required(custom_password_change_view)


class PasswordChangedView(TemplateView):

    template_name = 'profiles/password_changed.html'


password_changed_view = PasswordChangedView.as_view()
password_changed_view = login_required(password_changed_view)
