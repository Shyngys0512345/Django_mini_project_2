from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def clear_cache(sender, instance, **kwargs):
    cache.delete('student_profile_{}'.format(instance.pk))
