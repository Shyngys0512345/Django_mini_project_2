from django.db import models
from students.models import Student
from courses.models import Course

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    date = models.DateField(verbose_name="Дата")
    status = models.BooleanField(default=False, verbose_name="Статус присутствия")

    def __str__(self):
        return f'{self.student.name} - {self.course.name} - {"Присутствовал" if self.status else "Отсутствовал"}'
