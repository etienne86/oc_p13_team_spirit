from django.urls import path

from teamspirit.profiles.views import (
    custom_password_change_view,
    custom_password_reset_complete_view,
    custom_password_reset_confirm_view,
    custom_password_reset_done_view,
    custom_password_reset_view,
    password_changed_view,
    profile_view,
    update_personal_info_view,
    update_phone_address_view,
)

app_name = 'profiles'

urlpatterns = [
    path('', profile_view, name="profile"),
    path(
        'change_password/',
        custom_password_change_view,
        name="change_password"
    ),
    path(
        'change_password/done/',
        password_changed_view,
        name="change_password_done"
    ),
    path(
        'reset_password/',
        custom_password_reset_view,
        name="reset_password"
    ),
    path(
        'reset_password/done/',
        custom_password_reset_done_view,
        name="reset_password_done"
    ),
    path(
        'reset_password_confirm/<uidb64>/<token>/',
        custom_password_reset_confirm_view,
        name="reset_password_confirm"
    ),
    path(
        'reset_password_complete/',
        custom_password_reset_complete_view,
        name="reset_password_complete"
    ),
    path(
        'update_personal_info/',
        update_personal_info_view,
        name="update_personal_info"
    ),
    path(
        'update_phone_address/',
        update_phone_address_view,
        name="update_phone_address"
    ),
]
