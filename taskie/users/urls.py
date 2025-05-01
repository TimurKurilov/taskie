from django.urls import path
from .views import CreationView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "auth"

urlpatterns = [
    path('', LoginView.as_view(template_name="auth/login.html"), name="login"),
    path('register/', CreationView.as_view(), name='register'),
    path(
        'logout/',
        LogoutView.as_view(template_name="auth/logged_out.html"),
        name='logout'
    ),
]
