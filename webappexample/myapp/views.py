import json

from django.shortcuts import render


def index(request):
    return render(
        request,
        "myapp/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )
