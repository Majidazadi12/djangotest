from django.urls import path

from everycheese.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
