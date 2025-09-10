from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('auth/', include('users.urls', namespace='auth')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path("profile/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("upload/", include('upload.urls', namespace='upload')),
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
