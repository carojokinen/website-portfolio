from django.urls import path
from . import views

ulrpatterns = [
    path('', views.post_list, name='post_list'),
]