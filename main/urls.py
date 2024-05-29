from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('checklist/', views.checklist, name='checklist'),
    path('checklist_main/', views.checklist_main, name='checklist_main'),
    path('upload/', views.index, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)