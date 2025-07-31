from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cv/', views.cv_view, name='cv'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail'),
]
