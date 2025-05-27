from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path('', views.task_list, name="task_list"),
    path('create/', views.task_create_view, name="task_create"),
    path('<int:id>/', views.task_info, name="task_info")
]
