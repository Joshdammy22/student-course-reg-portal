from django.db import models
from users.models import Student

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    lecturer = models.CharField(max_length=50, unique=True)
    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title


