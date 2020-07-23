from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from teamspirit.profiles.forms import (
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)


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


class CustomPasswordResetView(PasswordResetView):

    template_name = 'profiles/reset_password/password_reset.html'
    form_class = CustomPasswordResetForm
    subject_template_name = 'profiles/reset_password/' \
        'password_reset_subject.txt'
    email_template_name = 'profiles/reset_password/password_reset_email.html'
    success_url = 'done'


custom_password_reset_view = CustomPasswordResetView.as_view()


class CustomPasswordResetDoneView(PasswordResetDoneView):

    template_name = 'profiles/reset_password/password_reset_done.html'


custom_password_reset_done_view = CustomPasswordResetDoneView.as_view()


class CustomPasswordResetConfirmView(PasswordResetConfirmView):

    template_name = 'profiles/reset_password/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('profiles:reset_password_complete')


custom_password_reset_confirm_view = CustomPasswordResetConfirmView.as_view()


class CustomPasswordResetCompleteView(PasswordResetCompleteView):

    template_name = 'profiles/reset_password/password_reset_complete.html'


custom_password_reset_complete_view = CustomPasswordResetCompleteView.as_view()
