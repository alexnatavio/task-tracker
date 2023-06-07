from django.shortcuts import render
from projects.models import Project
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project_object": project}

    return render(request, "projects/detail.html", context)


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
