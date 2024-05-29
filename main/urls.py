from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checklist/', views.checklist, name='checklist'),
    path('checklist_main/', views.checklist_main, name='checklist_main'),
]