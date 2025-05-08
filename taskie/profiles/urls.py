from django.urls import path
from . import views 

app_name = "profile"

urlpatterns = [
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/edit/", views.edit_profile, name="edit_profile")
]
