from django.shortcuts import render, redirect
from my_website.models import *
from my_website.forms import *


# Create your views here.
def home(request):
    projects = Projects.objects.all()
    skills = Skills.objects.all()

    context = {"projects": projects, "skills": skills}
    return render(request, "index.html", context)


def projects(request):
    projects = Projects.objects.all()

    context = {"projects": projects}
    return render(request, "projects.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def project_page(request, pk):
    project = Projects.objects.get(id=pk)

    context = {"project": project}
    return render(request, "post.html", context)


def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "project_form.html", context)


def edit_project(request, pk):
    p = Projects.objects.get(id=pk)


    form = ProjectForm(instance=p)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "project_form.html", context)
