from django.urls import path
from .views import log_in, caretakerpage, delete_user

urlpatterns = [
    path('', log_in, name='login'),
    path('caretakerpage/', caretakerpage, name='caretakerpage'),
    path('delete_user/<int:caretaker_id>', delete_user, name='deleteCaretaker'),

]