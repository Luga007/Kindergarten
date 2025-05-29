from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inventory
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Inventory)
def notify_if_low_stock(sender, instance, **kwargs):
    if instance.overall_kg < 10:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "alerts",
            {
                "type": "send_alert",
                "message": f"Внимание! Запас {instance.ingredients.name} упал ниже 10 кг: осталось {instance.overall_kg} кг"
            }
        )

