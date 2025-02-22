from django.urls import path
from . import views

urlpatterns = [
    path("", views.access_page, name="access_page"),
]
