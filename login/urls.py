from django.urls import path
from . import views

urlpatterns = [
    path("", views.test_login_page, name="login_page"),
]
