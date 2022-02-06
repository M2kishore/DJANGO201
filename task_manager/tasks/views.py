from dataclasses import field
from re import template

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

from tasks.models import Task


class UserLoginView(LoginView):
    template_name = "user_login.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "user_create.html"
    success_url = "/user/login"


def session_storage_view(request):
    total_views = request.session.get("total_views", 0)
    request.session["total_views"] = total_views + 1
    return HttpResponse(f"Total views is {total_views} and user is {request.user}")


class GenericTaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = "/tasks/"


class GenericTaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskCreateForm(ModelForm):
    def clean_title(self):
        title = self.cleaned_data["title"]
        print(title)
        if len(title) < 10:
            raise ValidationError("The data is too small")
        return title

    class Meta:
        model = Task
        fields = ("title", "description", "completed")


class GenericTaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "task_update.html"
    success_url = "/tasks"


class GenerivTaskCreateView(CreateView):
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = "/tasks"


class GenericTaskView(ListView):
    queryset = Task.objects.filter(deleted=False)
    template_name = "tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        tasks = Task.objects.filter(deleted=False)
        search_string = self.request.GET.get("search")
        if search_string:
            tasks = tasks.filter(title__icontains=search_string)
        return tasks


class CreateTaskView(View):
    def get(self, request):
        return render(request, "task_create.html")

    def post(self, request):
        task_string = request.POST.get("task")
        task_obj = Task(title=task_string)
        task_obj.save()
        return HttpResponseRedirect("/tasks")


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
