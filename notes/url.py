from django.urls import path

from . import views

app_name="notes"

urlpatterns = [
    path("", views.note_list, name="note_list" ),
    path("/<slug:slug>", views.note_create, name="note_create" ),
    path("/render_html/<slug:slug>", views.render_html, name="render_html" ),

]
