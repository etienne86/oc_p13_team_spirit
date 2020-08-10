from django.db.models import fields
from teamspirit.core.models import Address
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, HTML, Layout, Submit
from django.contrib.auth import forms as auth_forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from teamspirit.core.models import Address
from teamspirit.users.models import User


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-password-change-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', _('Change password')))


class CustomPasswordResetForm(auth_forms.PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-password-reset-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', _('Reset my password')))


class CustomSetPasswordForm(auth_forms.SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-set-password-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', _('Set Password')))


class UpdatePersonalInfoForm(ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UpdatePersonalInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-update-personal-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('last_name', value=self.user.last_name),
            Field('first_name', value=self.user.first_name)
        )
        self.helper.add_input(Submit('submit', 'Mettre à jour'))
        if self.is_valid():
            self.save()

    def save(self, commit=True):
        last_name = self.cleaned_data["last_name"]
        first_name = self.cleaned_data["first_name"]
        if commit:
            self.user.last_name = last_name.upper()
            self.user.first_name = first_name.capitalize()
            self.user.save()
        return self.user


class UpdatePhoneAddressForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UpdatePhoneAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-update-personal-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        # self.helper.layout = Layout(
        #     Field('label_first', value=self.user.personal.address.label_first),
        #     Field(
        #         'label_second',
        #         value=self.user.personal.address.label_second
        #     ),
        #     Field('postal_code', value=self.user.personal.address.postal_code),
        #     Field('city', value=self.user.personal.address.city),
        #     Field('country', value=self.user.personal.address.country),
        # )
        self.helper.add_input(Submit('submit', 'Mettre à jour'))
        if self.is_valid():
            self.save()

    def save(self, commit=True):
        # phone_number = self.cleaned_data["phone_number"]
        label_first = self.cleaned_data["label_first"]
        label_second = self.cleaned_data["label_second"]
        postal_code = self.cleaned_data["postal_code"]
        city = self.cleaned_data["city"]
        country = self.cleaned_data["country"]
        if commit:
            # self.user.personal.phone_number = phone_number
            self.user.personal.address.label_first = label_first
            self.user.personal.address.label_second = label_second
            self.user.personal.address.postal_code = postal_code
            self.user.personal.address.city = city
            self.user.personal.address.country = country
            self.user.save()
        return self.user
