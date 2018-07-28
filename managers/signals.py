from django.contrib.auth.models import User
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver

from .models import Manager

@receiver(post_save, sender=User)
def create_user_manager(sender, instance, created, **kwargs):
  if created:
    Manager.objects.create(user=instance)

@receiver(pre_save, sender=User)
def save_user_manager(sender, instance, **kwargs):
    instance.Manager.save()