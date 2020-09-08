from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from teamspirit.profiles.forms import (
    AddressForm,
    ConfidentialityForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
    PersonalInfoForm,
    PhoneForm,
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


class PersonalInfoView(FormView):

    template_name = 'profiles/update_personal_info.html'
    form_class = PersonalInfoForm
    success_url = reverse_lazy('profiles:profile')

    def get_form_kwargs(self):
        kwargs = super(PersonalInfoView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


personal_info_view = PersonalInfoView.as_view()
personal_info_view = login_required(personal_info_view)


class PhoneView(FormView):

    template_name = 'profiles/update_phone.html'
    form_class = PhoneForm
    success_url = reverse_lazy('profiles:profile')

    def get_form_kwargs(self):
        kwargs = super(PhoneView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


update_phone_view = PhoneView.as_view()
update_phone_view = login_required(update_phone_view)


class AddressView(FormView):

    template_name = 'profiles/update_address.html'
    form_class = AddressForm
    success_url = reverse_lazy('profiles:profile')

    def get_form_kwargs(self):
        kwargs = super(AddressView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


address_view = AddressView.as_view()
address_view = login_required(address_view)


class ConfidentialityView(FormView):

    template_name = 'profiles/update_confidentiality.html'
    form_class = ConfidentialityForm
    success_url = reverse_lazy('profiles:profile')

    def get_form_kwargs(self):
        kwargs = super(ConfidentialityView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


confidentiality_view = ConfidentialityView.as_view()
confidentiality_view = login_required(confidentiality_view)


@login_required
def phone_address_view(request):
    context = {}
    if request.method == 'POST':
        phone_form = PhoneForm(request.POST, user=request.user)
        address_form = AddressForm(request.POST, user=request.user)
        confidentiality_form = ConfidentialityForm(
            request.POST,
            user=request.user
        )
        if all([
            phone_form.is_valid(),
            address_form.is_valid(),
            confidentiality_form.is_valid()
        ]):
            # process forms
            phone_form.save()
            address_form.save()
            confidentiality_form.save()
            # redirect to the profile url
            return redirect(reverse_lazy('profiles:profile'))
    else:
        phone_form = PhoneForm(user=request.user)
        address_form = AddressForm(user=request.user)
        confidentiality_form = ConfidentialityForm(user=request.user)
    context['phone_form'] = phone_form
    context['address_form'] = address_form
    context['confidentiality_form'] = confidentiality_form
    return render(
        request,
        'profiles/update_phone_address.html',
        context,
    )
