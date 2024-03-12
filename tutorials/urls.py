from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tutorials, name='view_tutorials'),
    path('edit_tutorial/<int:tutorial_id>/',
         views.edit_tutorial, name='edit_tutorial'),
    path('add_tutorial/', views.add_tutorial, name='add_tutorial'),
    path('delete_tutorial/<int:tutorial_id>/',
         views.delete_tutorial, name='delete_tutorial'),
]
