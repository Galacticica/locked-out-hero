from django.urls import path
from . import views

urlpatterns = [
    path("", views.access_page, name="access_page"),
    path("access_granted/", views.access_granted, name="access_granted"),
    path("timed_logout/", views.timed_logout, name="timed_logout"),
    # other paths...
]
