from django.urls import path
from tasks.views import create_task, task_detail

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_detail, name="show_my_tasks"),
]
