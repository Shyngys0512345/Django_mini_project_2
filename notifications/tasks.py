# notifications/tasks.py

from students.models import Student
from grades.models import Grade
from attendance.models import Attendance
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def daily_attendance_reminder():
    students = Student.objects.all()
    for student in students:
        send_mail(
            'Attendance Reminder',
            'Please mark your attendance for today.',
            'from@example.com',
            [student.email],
        )
    return f'Sent reminders to {students.count()} students.'

@shared_task
def grade_update_notification(student_id, grade):
    student = Student.objects.get(id=student_id)
    send_mail(
        'Grade Update',
        f'Your new grade is: {grade}',
        'from@example.com',
        [student.email],
    )
    return f'Sent grade update to {student.email}.'
