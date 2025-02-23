from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q


def test_login_page(request):
    """Create a view for the login page."""
    template = loader.get_template("login/login.html")
    context = {}
    return HttpResponse(template.render(context, request))
