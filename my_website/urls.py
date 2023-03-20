from django.contrib import admin
from django.urls import path

from my_website import views

urlpatterns = [
    path('', views.home,name="home"),
    path('projects/', views.projects,name="projects"),
    path('about/', views.about,name="about"),
    path('contacts/', views.contact,name="contacts"),

    path('project/<str:pk>/', views.project_page, name="project-page"),
    path('create_project/', views.create_project, name="create-project"),
    path('edit_project/<str:pk>/', views.edit_project, name="edit-project"),

]
