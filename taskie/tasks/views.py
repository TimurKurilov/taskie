from django.shortcuts import render, redirect
from .forms import TasksForm
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@login_required
def task_create_view(request):
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/tasks/")
    else:
        form = TasksForm()
    
    return render(request, "tasks/create_task.html", {"form": form})


def task_list(request):
    tasks = Tasks.objects.all().order_by("id")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def task_info(request, id):
    task = get_object_or_404(Tasks, id=id)
    return render(request, "tasks/task_info.html", {"task": task})

@login_required
def task_edit(request, id):
    task = get_object_or_404(Tasks, id=id)

    if task.user != request.user:
        return redirect("/tasks/")

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = TasksForm(instance=task)

    return render(request, "tasks/task_edit.html", {"form": form, "task": task})
