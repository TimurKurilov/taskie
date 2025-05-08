from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('auth/', include('users.urls', namespace='auth')),
    path("profile/", include(("profiles.urls", "profiles"), namespace="profiles"))
]
