from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index" ),
    path("index.html", views.index, name="index2" ),
    path("login.html", views.login, name="login"),
    path("account/", views.dashboard, name="dashboard"),
    path("account/index.html", views.dashboard, name="dashboard2")

]
