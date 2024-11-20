from django.db import models
from students.models import Student

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    instructor = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата зачисления")

    def __str__(self):
        return f'{self.student.name} - {self.course.name}'
