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
    return render(request, "project_page.html", context)


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
    project = Projects.objects.get(id=pk)

    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "project_form.html", context)


def messages(request):
    messages = Messages.objects.all()
    context = {"messages": messages}
    return render(request, "inbox.html", context)


def view_message(request, pk):
    message = Messages.objects.get(id=pk)
    context = {"message": message}
    return render(request, "message.html", context)

def delete_project(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": object}
    return render(request, "delete.html", context)
