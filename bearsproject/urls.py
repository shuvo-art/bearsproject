from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bearsapp.views import CourseViewSet, EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
