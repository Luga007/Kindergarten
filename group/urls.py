from django.urls import path
from . views import group_data_page, delete_group

urlpatterns = [
    path('', group_data_page, name='group_data_page'),
    path('delete_group/<int:group_id>', delete_group, name='delete_group'),
]