from django.views import View

from django.http.response import JsonResponse

from tasks.models import Task

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "completed"]


class TaskListAPI(APIView):
    def get(self, response):
        tasks = Task.objects.filter(deleted=False)
        data = TaskSerializer(tasks, many=True).data
        return Response({"tasks": data})
