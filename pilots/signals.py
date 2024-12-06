from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from pilots.models import Pilot, PilotInventory


def pilot_inventory_update():
    pilots_count = Pilot.objects.all().count()
    pilots_value = Pilot.objects.aggregate(
        market_cap = Sum('market_value')
    ) ['market_cap']

    PilotInventory.objects.create(
        pilots_count = pilots_count,
        pilots_value = pilots_value
    )

@receiver(post_delete, sender=Pilot)
def pilot_post_delete(sender, instance, **kwargs):
   pilot_inventory_update()

@receiver(post_save, sender=Pilot)
def pilot_post_save(sender, instance, **kwargs):
    pilot_inventory_update()

