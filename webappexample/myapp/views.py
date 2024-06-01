import json

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(
        request,
        "myapp/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def dashboard(request):
    if not request.session.get("user"):
        return redirect_to_login(
            request.build_absolute_uri(), reverse("accounts:login")
        )

    return render(request, "myapp/dashboard.html")
