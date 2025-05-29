from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Kids


@receiver(post_save, sender=Kids)
def increase_kids_count(sender, instance, created, **kwargs):
    if created:
        group = instance.group
        group.total_quantity += 1
        group.save()


@receiver(post_delete, sender=Kids)
def decrease_kids_count(sender, instance, **kwargs):
    group = instance.group
    group.total_quantity -= 1
    group.save()
