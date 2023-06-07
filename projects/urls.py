from django.urls import path
from django.contrib import admin
from projects.views import project_list, project_detail, create_project


urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", create_project, name="create_project"),
]
