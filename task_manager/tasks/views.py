from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

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