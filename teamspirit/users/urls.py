from django.contrib.auth.views import LoginView
from django.urls import path

from teamspirit.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login"
    ),
    path("~redirect/", user_redirect_view, name="redirect"),
    path("~update/", user_update_view, name="update"),
    path("<str:email>/", user_detail_view, name="detail"),
]
