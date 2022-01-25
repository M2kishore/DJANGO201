from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render

tasks = []
completed_tasks = []


def task_view(request):
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_string = request.GET.get("task")
    tasks.append(task_string)
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    del tasks[index - 1]
    return HttpResponseRedirect("/tasks")


def complete_task(requests, index):
    # moving task from tasks to completed tasks
    task_string = tasks[index - 1]
    del tasks[index - 1]
    completed_tasks.append(task_string)
    return HttpResponseRedirect("/tasks")


def completed_task_view(request):
    return render(request, "completed_tasks.html", {"tasks": completed_tasks})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>", delete_task_view),
    path("complete_task/<int:index>", complete_task),
    path("completed_tasks/", completed_task_view)
    # Add all your views here
]
