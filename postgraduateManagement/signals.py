from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender = Profile)
def add_user_to_admin_group(sender, instance, created, ** kwargs):
    if created:
        try:
            admin = Group.objects.get(name = 'administracion')
        except Group.DoesNotExist:
            admin = Group.objects.create(name = 'administracion')
            instance.user.groups.add(admin)