from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes, name='routes'),
    path('projects/', views.projects, name="rest_projects"),
    path('project/<int:product_id>/', views.project, name='rest_project'),
    path('register-user/', views.user_registration, name='user-registration'),
    path('users/', views.users, name='users-rest')
]
