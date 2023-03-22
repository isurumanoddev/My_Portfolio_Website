from django.shortcuts import render, redirect
from my_website.models import *
from my_website.forms import *
from django.contrib import messages


# Create your views here.
def home(request):
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.info(request, "Message sent Successfully")
            return redirect("home")

    context = {"projects": projects, "skills": skills, "form": form}
    return render(request, "index.html", context)


def projects(request):
    projects = Projects.objects.all()

    context = {"projects": projects}
    return render(request, "projects.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)


def project_page(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == "POST":
        Comments.objects.create(
            project=project,
            name="Anonymous",
            body=request.POST.get("message")

        )
        return redirect("project-page", pk=project.id)
    comments = project.comments_set.all().order_by("-created")
    comment_count = project.comments_set.count()

    context = {"project": project, "comments": comments, "comment_count": comment_count}
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


def inbox_messages(request):
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


def create_skill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "skill_form.html", context)


def donation(request):
    context = {}
    return render(request, "donation.html", context)
