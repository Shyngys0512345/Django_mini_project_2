import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

logger = logging.getLogger('custom')

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    logger.info(f"User {user.username} logged in.")

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    logger.info(f"User {user.username} logged out.")
