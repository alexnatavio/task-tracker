from django.shortcuts import render
from projects.models import Project
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)
