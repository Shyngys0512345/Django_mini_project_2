from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Course


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Math 101",
            description="Basic Math Course"
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Math 101")
        self.assertEqual(self.course.description, "Basic Math Course")


class CourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(
            name="Math 101",
            description="Basic Math Course"
        )

    def test_get_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        data = {"name": "Physics 101", "description": "Basic Physics Course"}
        response = self.client.post('/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_course(self):
        data = {"description": "Advanced Math Course"}
        response = self.client.patch(f'/courses/{self.course.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.description, "Advanced Math Course")

    def test_delete_course(self):
        response = self.client.delete(f'/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
