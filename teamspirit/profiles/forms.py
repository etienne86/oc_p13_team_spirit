from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import forms
from django.utils.translation import ugettext_lazy as _


class CustomPasswordChangeForm(forms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-authentication-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', _('Change password')))
