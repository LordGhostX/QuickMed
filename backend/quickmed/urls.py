from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index2"),
    path("login.html", views.login, name="login"),
    path("account/logout.html", views.logout, name= "logout"),
    path("account/", views.dashboard, name="dashboard"),
    path("account/index.html", views.dashboard, name="dashboard2"),
    path("account/tests.html", views.taketest, name="taketest"),
    path("account/statistics.html", views.statistics, name="statistics"),
    path("account/settings.html", views.settings, name="settings"),
    path("account/contact.html", views.contact, name="contact"),
    path("account/billing.html", views.billing, name="billing"),
    path("account/results.html", views.test_history, name="test_history"),
    path("account/test-malaria.html", views.test_malaria, name="malaria_test"),
    path("account/logout.html", views.logout, name="logout")
]
