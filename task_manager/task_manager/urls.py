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
from tasks.views import (
    CreateTaskView,
    GenericTaskDetailView,
    GenericTaskUpdateView,
    GenericTaskView,
    GenericTaskCreateView,
    GenericTaskDeleteView,
    session_storage_view,
    UserCreateView,
    UserLoginView,
    TaskView,
    TestView,
    TestStaticView,
    add_task_view,
    delete_task_view,
    task_view,
)

from tasks.apiViews import TaskListAPI

from django.contrib.auth.views import LogoutView

from tasks.apiViews import TaskViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("api/tasks", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", GenericTaskView.as_view()),
    path("tasksapi/", TaskListAPI.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("update-task/<pk>", GenericTaskUpdateView.as_view()),
    path("detail-task/<pk>", GenericTaskDetailView.as_view()),
    path("delete-task/<pk>", GenericTaskDeleteView.as_view()),
    path("user/signup/", UserCreateView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("sessiontest", session_storage_view),
    path("add-task/", add_task_view),
    path("test/", TestView.as_view()),
    path("test-static/", TestStaticView.as_view()),
    # path("delete-task/<int:id>/", delete_task_view),
] + router.urls
