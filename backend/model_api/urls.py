from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="api_index"),
    path("malaria/", views.malaria, name="malaria_test")
]
