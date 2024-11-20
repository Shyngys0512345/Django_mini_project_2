from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Добавьте дополнительные поля, если требуется
    user_type = models.CharField(max_length=10, choices=(('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')))

from django.http import HttpResponseForbidden

def some_view(request):
    if not request.user.is_authenticated or request.user.user_type != 'admin':
        return HttpResponseForbidden("Вы не имеете доступа к этой функции")
    # Основная логика функции
