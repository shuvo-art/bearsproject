from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    price = models.FloatField()  # assuming USD
    class Meta:
        app_label = 'bearsapp'

class Enrollment(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    class Meta:
        app_label = 'bearsapp'