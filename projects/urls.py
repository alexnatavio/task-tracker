from django.urls import path
from django.contrib import admin
from projects.views import project_list, project_detail


urlpatterns = [
    path("projects", project_list, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
]
