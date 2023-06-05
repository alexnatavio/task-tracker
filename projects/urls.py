from django.urls import path, include
from django.contrib import admin
from projects.views import project_list


urlpatterns = [
    path("", project_list, name="list_projects"),
]
