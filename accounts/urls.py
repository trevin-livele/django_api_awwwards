from django.urls import path
from  .import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('createpost/', views.createpost, name='createpost'),

]