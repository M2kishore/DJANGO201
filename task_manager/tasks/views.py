from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from django.views import View
from django.views.generic.list import ListView


class GenericTaskView(ListView):
    model = Task
    template_name = "tasks.html"
    context_object_name = "tasks"


class TaskView(View):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        search_string = request.GET.get("search")
        if search_string:
            tasks = tasks.filter(title__icontains=search_string)
        return render(request, "tasks.html", {"tasks": tasks})

    def post():
        pass


def task_view(request):
    tasks = Task.objects.filter(deleted=False)
    search_string = request.GET.get("search")
    if search_string:
        tasks = tasks.filter(title__icontains=search_string)
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(request):
    task_string = request.GET.get("task")
    Task(title=task_string).save()
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, id):
    Task.objects.filter(id=id).update(deleted=True)
    return HttpResponseRedirect("/tasks/")