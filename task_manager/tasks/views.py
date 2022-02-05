from dataclasses import field
from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView


from django.forms import ModelForm


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