from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from allauth.account.forms import LoginForm
from allauth.account.views import LoginView


class CustomLoginView(LoginView):
    template_name = "login/login.html"


def login_page(request):
    """Create a view for the login page."""
    template = loader.get_template("login/login.html")
    form = LoginForm()
    context = {"login_form": form}
    return HttpResponse(template.render(context, request))
