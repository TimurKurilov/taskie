from django.shortcuts import render, redirect
from .forms import TasksForm
from .models import Tasks
from django.contrib.auth.decorators import login_required

@login_required
def task_create_view(request):
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TasksForm()
    
    return render(request, "tasks/create_task.html", {"form": form})


def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})
