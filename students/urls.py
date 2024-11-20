from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('student/', StudentAPIView.as_view(), name='student-api'),
]
