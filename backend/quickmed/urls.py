from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index2"),
    path("register.html", views.register, name="register"),
    path("login.html", views.login, name="login"),
    path("account/logout.html", views.logout, name="logout"),
    path("account/", views.redirect_dashboard, name="dashboard"),
    path("account/index.html", views.dashboard, name="dashboard2"),
    path("account/tests.html", views.taketest, name="taketest"),
    path("account/statistics.html", views.statistics, name="statistics"),
    path("account/settings.html", views.edit_user_profile, name="settings"),
    path("account/contact.html", views.contact, name="contact"),
    path("account/billing.html", views.billing, name="billing"),
    path("account/results.html", views.test_history, name="test_history"),
    path("account/test-malaria.html", views.test_malaria, name="malaria_test"),
    path("account/get_result.html", views.get_result, name="result_page"),
    path("account/test-xray.html", views.test_xray, name="xray_test"),
    path("account/test-skin-cancer.html", views.test_skin_cancer, name="skin_cancer_test"),
    path("account/test-oct.html", views.test_oct, name="skin_oct"),
    path("account/logout.html", views.logout, name="logout"),
    path("account/billing-history.html", views.billing_history, name="billing_history")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
