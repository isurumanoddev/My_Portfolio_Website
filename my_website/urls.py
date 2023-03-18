from django.contrib import admin
from django.urls import path

from my_website import views

urlpatterns = [
    path('', views.home,name="home"),
    path('projects/', views.projects,name="projects"),

]
