from django.urls import path
from .views import attendance_page, delete_attendance

urlpatterns = [
    path('', attendance_page, name='attendance_page'),
    path('delete_attendance/<int:attendance_id>', delete_attendance, name='delete_attendance'),
]