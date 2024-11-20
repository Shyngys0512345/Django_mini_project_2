from django.shortcuts import render
from .models import Grade
from .serializers import GradeSerializer
from rest_framework import viewsets

# Create your views here.

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer