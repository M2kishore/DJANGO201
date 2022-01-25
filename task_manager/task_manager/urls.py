"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

tasks = []


def task_view(request):
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_string = request.GET.get("task")
    tasks.append(task_string)
    return HttpResponseRedirect("tasks")


def delete_task_view(request, index):
    del tasks[index - 1]
    return HttpResponseRedirect("/tasks")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks", task_view),
    path("add-task", add_task_view),
    path("delete-task/<int:index>", delete_task_view),
]
