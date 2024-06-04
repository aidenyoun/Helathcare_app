from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checklist/', views.checklist, name='checklist'),
    path('checklist_main/', views.checklist_main, name='checklist_main'),
    path('upload/', views.index, name='upload'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('get-records/', views.get_records, name='get_records'),
    path('delete-record/<int:record_id>/', views.delete_record, name='delete_record'),  # Added delete record URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
