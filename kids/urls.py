from django.urls import path
from .views import kid_data_page, kid_delete, parent_page, parent_delete
urlpatterns = [
    path('', kid_data_page, name='kids_page'),
    path('delete/<int:kid_id>', kid_delete, name='kids_delete'),

    path('parent_page/', parent_page, name='parent_page'),
    path('parent_delete/<int:parent_id>', parent_delete, name='parent_delete'),
]