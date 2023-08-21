from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from event.models import EventDetails
from .models import Notification

@receiver(post_save, sender=EventDetails)
def create_notification(sender, instance, created, **kwargs):
    if created:
        creator_info = instance.creator
        notification_content = f"A new event '{instance.EventName}' has been created."
        Notification.objects.create(event=instance, content=notification_content,creator_info=creator_info)
@receiver(post_delete, sender=EventDetails)
def delete_notifications(sender, instance, **kwargs):
    # Delete notifications associated with the deleted event
    Notification.objects.filter(event=instance).delete()
