from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tutorials, name='view_tutorials'),
]
