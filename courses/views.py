from django.shortcuts import render
from .permissions import IsTeacherOrReadOnly, IsAdminUser
from .models import Course
from .serializers import CourseSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class CourseAPIView(APIView):
    permission_classes = [IsTeacherOrReadOnly]

    def post(self, request):
        # Только учителя могут добавлять курсы
        # Логика добавления курса
        return Response({"message": "Курс добавлен"})


class AdminAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Действия для администраторов
        return Response({"message": "Доступные данные для администрации"})

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @method_decorator(cache_page(60*15))  # Кэширует страницу на 15 минут
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        course = serializer.save()
        logger.info(f"Course {course.name} created by {self.request.user.username}.")
