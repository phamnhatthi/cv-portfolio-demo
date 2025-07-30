from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ajax/contact/', views.ajax_contact, name='ajax_contact'),
]
