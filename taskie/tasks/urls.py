from django.urls import path
from tasks import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.task_create_view, name="task_create"),
    path("<int:id>/edit/", views.task_edit, name="task_edit"),
    path("<int:id>/", views.task_info, name="task_info"),
    path("<int:id>/take/", views.take_task, name='take_task'),
    path("<int:id>/end/", views.end_task, name='end_task'),
    path('<int:id>/chat', views.chat, name="chat")

]
