from django.urls import path
from  .import views


urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('submit_review/<int:post_id>', views.submit_review, name='submit_review'),
    path('singleview/', views.singleview, name='singleview'),


]