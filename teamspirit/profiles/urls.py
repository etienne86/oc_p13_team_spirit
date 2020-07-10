from django.urls import path

from teamspirit.profiles.views import (
    custom_password_change_view,
    password_changed_view,
    profile_view,
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
    )
]
