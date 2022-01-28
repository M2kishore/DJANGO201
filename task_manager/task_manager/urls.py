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
from re import search
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from tasks.models import Task


def task_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.all()
    if search_term:
        tasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_string = request.GET.get("task")
    Task(title=task_string).save()
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, id):
    Task.objects.filter(id).delete()
    return HttpResponseRedirect("/tasks")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", task_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:id>/", delete_task_view),
]
