from django.urls import path
from . import views 

app_name = "profile"

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("<str:username>/edit/", views.edit_profile, name="edit_profile"),
    path("<str:username>/", views.profile, name="profile"),
]