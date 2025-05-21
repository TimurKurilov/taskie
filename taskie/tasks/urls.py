from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path('', views.task_list, name="task_list"),
    path('create/', views.task_create_view, name="task_create")
    #path('task/<int:id>/', views.task_create_view, name="task_create")
]
