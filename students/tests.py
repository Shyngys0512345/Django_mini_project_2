from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from students.models import Student


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Test Student",
            email="test@student.com",
            dob="2000-01-01"
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.email, "test@student.com")
        self.assertEqual(str(self.student), "Test Student")


class StudentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(
            name="Test Student",
            email="test@student.com",
            dob="2000-01-01"
        )

    def test_get_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        data = {"name": "New Student", "email": "new@student.com", "dob": "2001-01-01"}
        response = self.client.post('/students/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_student(self):
        data = {"name": "Updated Student"}
        response = self.client.patch(f'/students/{self.student.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "Updated Student")

    def test_delete_student(self):
        response = self.client.delete(f'/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# students/tests.py
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from students.models import Student


class RolePermissionsTest(TestCase):
    def setUp(self):
        # Создаем пользователей
        self.admin = User.objects.create_superuser(username="admin", password="admin123")
        self.teacher = User.objects.create_user(username="teacher", password="teacher123", is_staff=True)
        self.student_user = User.objects.create_user(username="student", password="student123")
        self.student = Student.objects.create(
            name="Test Student",
            email="test@student.com",
            dob="2000-01-01"
        )
        self.client = APIClient()

    def test_admin_access(self):
        self.client.login(username="admin", password="admin123")
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_access(self):
        self.client.login(username="teacher", password="teacher123")
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_student_access(self):
        self.client.login(username="student", password="student123")
        response = self.client.get(f'/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# students/tests.py
from django.core.cache import cache
from students.models import Student
from django.test import TestCase


class CacheTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Cached Student",
            email="cached@student.com",
            dob="2000-01-01"
        )

    def test_cache_student_profile(self):
        cache.set(f'student_profile_{self.student.id}', {"name": "Cached Student"}, timeout=60)
        cached_data = cache.get(f'student_profile_{self.student.id}')
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data['name'], "Cached Student")

    def test_cache_invalidation(self):
        cache.set(f'student_profile_{self.student.id}', {"name": "Cached Student"}, timeout=60)
        cache.delete(f'student_profile_{self.student.id}')
        cached_data = cache.get(f'student_profile_{self.student.id}')
        self.assertIsNone(cached_data)
