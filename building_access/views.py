from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Count
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Building


@login_required
def access_page(request):
    """Create a view for the usage page."""

    user = request.user
    current_time = datetime.now().time()
    accessible_buildings = Building.objects.filter(
        Q(name=user.dorm) | Q(start_time__lte=current_time, end_time__gte=current_time)
    )

    print(accessible_buildings)
    template = loader.get_template("building_access/access.html")
    context = {}
    return HttpResponse(template.render(context, request))
