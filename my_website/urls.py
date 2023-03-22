from django.contrib import admin
from django.urls import path

from my_website import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contact, name="contacts"),
    path('messages/', views.inbox_messages, name="messages"),
    path('message/<str:pk>', views.view_message, name="view-message"),

    path('project/<str:pk>/', views.project_page, name="project-page"),
    # path('project/<str:pk>/', views.project_page, name="project-page"),
    # path('project/<str:pk>/', views.project_page, name="project-page"),


    path('create_project/', views.create_project, name="create-project"),
    path('edit_project/<str:pk>/', views.edit_project, name="edit-project"),
    path('delete_project/<str:pk>/', views.delete_project, name="delete-project"),

    path('create_skill/', views.create_skill, name="create-skill"),

]
