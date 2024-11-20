from django.db import models
from students.models import Student
from courses.models import Course

# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    grade = models.CharField(max_length=2, verbose_name="Оценка")
    date = models.DateField(verbose_name="Дата выставления оценки")
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")

    def __str__(self):
        return f'{self.grade} - {self.student.name} - {self.course.name}'
