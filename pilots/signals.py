from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from pilots.models import Pilot

@receiver(pre_save, sender=Pilot)
def pilot_pre_save(sender, instance, **kwargs):
    print(' ### PRE SAVE ###')

@receiver(post_save, sender=Pilot)
def pilot_post_save(sender, instance, **kwargs):
    print(' ### PRE SAVE ###')