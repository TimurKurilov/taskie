from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "auth"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path(
        'logout/',
        LogoutView.as_view(template_name="auth/logged_out.html"),
        name='logout'
    ),
]
