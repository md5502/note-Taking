from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.create_user, name="create_user"),
    path("", include("django.contrib.auth.urls")),
]
