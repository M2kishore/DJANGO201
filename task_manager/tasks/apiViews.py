from django.views import View

from django.http.response import JsonResponse

from tasks.models import Task


class TaskListAPI(View):
    def get(self, response):
        tasks = Task.objects.filter(deleted=False)
        data = []
        for task in tasks:
            data.append({"title": task.title})
        return JsonResponse({"tasks": data})
