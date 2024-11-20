from django.shortcuts import render
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework import viewsets

# Create your views here.

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def perform_update(self, serializer):
        attendance = serializer.save()
        logger.info(f"Attendance updated for student {attendance.student.name} in course {attendance.course.name}.")
