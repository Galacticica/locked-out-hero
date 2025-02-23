from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import LetMeInForm
from django.contrib import messages
from access_log.add_log import add_log


@login_required
def access_page(request):
    """Create a view for the usage page."""

    user = request.user
    current_time = datetime.now().time()
    accessible_buildings = user.accessible_buildings.filter(
        Q(name=user.dorm) | Q(start_time__lte=current_time, end_time__gte=current_time)
    )

    if request.method == "POST":
        form = LetMeInForm(request.POST, queryset=accessible_buildings)

        if form.is_valid():
            building = form.cleaned_data["building"]
            user.times_used += 1
            user.save()
            add_log(building, user)
            messages.success(request, f"Successfully accessed {building.name}")
            return redirect("access_page")
    else:
        form = LetMeInForm(queryset=accessible_buildings)
    template = loader.get_template("building_access/access.html")
    context = {"building_select": form}
    return HttpResponse(template.render(context, request))
