from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="api_index"),
    path("malaria/", views.malaria, name="malaria_test"),
    path("skin_cancer/", views.skin_cancer, name="skin_cancer_test")
]
