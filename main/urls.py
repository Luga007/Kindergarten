from django.urls import path
from .views import main

urlpatterns = [
    path('main_page/', main, name='index'),
]