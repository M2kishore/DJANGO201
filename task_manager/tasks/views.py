from django.shortcuts import render

# Create your views here.
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
    return HttpResponseRedirect("tasks")
