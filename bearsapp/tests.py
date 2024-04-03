from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, Enrollment

class CoursesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_data = {
            'title': 'Test Course',
            'description': 'Test Course Description',
            'instructor': 'Test Instructor',
            'duration': 60,
            'price': 9.99
        }
        self.course = Course.objects.create(**self.course_data)
    # Add more test methods below
    def test_get_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one course is created in setup

    def test_create_course(self):
        response = self.client.post('/courses/', self.course_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)  # Assuming two courses after creation

    def test_get_course(self):
        response = self.client.get(f'/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.course_data['title'])

class CourseModelTest(TestCase):
    def setUp(self):
        self.course_data = {
            'title': 'Test Course',
            'description': 'Test Course Description',
            'instructor': 'Test Instructor',
            'duration': 60,
            'price': 9.99
        }

    def test_course_creation(self):
        course = Course.objects.create(**self.course_data)
        self.assertEqual(course.title, 'Test Course')


        def test_enrollment_creation(self):
        course = Course.objects.create(**self.course_data)
        enrollment_data = {
            'student_name': 'Test Student',
            'course': course,
            'enrollment_date': '2024-04-03'
        }
        enrollment = Enrollment.objects.create(**enrollment_data)
        self.assertEqual(enrollment.student_name, 'Test Student')