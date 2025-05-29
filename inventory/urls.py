from django.urls import path
from .views import inventory_page, delete_inventory, low_stock_alerts

urlpatterns = [
    path('', inventory_page, name='inventory_page'),
    path('delete_inventory<int:inventory_id>', delete_inventory, name='delete_inventory'),

    path('check/', low_stock_alerts, name='check_inventory_and_alert'),
]