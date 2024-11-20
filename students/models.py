from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    dob = models.DateField(verbose_name="Дата рождения")
    registration_date = models.DateField(verbose_name="Дата регистрации")

    def __str__(self):
        return self.name
