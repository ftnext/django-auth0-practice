from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("callback", views.callback, name="callback"),
]
