from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from notifications.tasks import daily_attendance_reminder


class CeleryTaskTest(TestCase):
    def test_daily_attendance_reminder(self):
        result = daily_attendance_reminder.delay()
        self.assertIsNotNone(result.id)
        result.get(timeout=10)  # Ожидаем выполнения
        self.assertTrue(result.successful())
