from django.urls import path

from auth0authorization import views

urlpatterns = [
    path("public", views.public),
]
