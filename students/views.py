from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Student
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .serializers import StudentSerializer
import logging

User = get_user_model()


class StudentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if not request.user.is_student:
            return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

        # Использование сериализатора для получения данных студента
        student = Student.objects.get(user=request.user)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @method_decorator(cache_page(60 * 10))  # Кэширует на 10 минут
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

logger = logging.getLogger('custom')

def get_cached_data(key):
    data = cache.get(key)
    if data:
        logger.info(f"Cache hit for key {key}.")
    else:
        logger.warning(f"Cache miss for key {key}.")
    return data