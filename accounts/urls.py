from django.urls import path
from  .import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),


]