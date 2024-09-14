from django.urls import path

from . import views

app_name = "grammar"
urlpatterns = [
    # Other URL patterns...
    path("check/<slug:slug>/", views.grammar_check, name="grammar_check"),
]
