from django.urls import path
from .views import *

app_name = 'Course'

urlpatterns = [
    path('', list_courses, name='list_courses'),
    path('create/', create_course, name='create_course'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/', student_course_detail, name='student_course_detail'),
    path('<int:course_id>/update/', update_course, name='update_course'),
    path('<int:course_id>/delete/', delete_course, name='delete_course'),
    path('student_courses/', student_courses, name='student_courses'),
    path('available/', available_courses, name='available_courses'),
    path('register/<int:course_id>/', register_course, name='register_course'),

]
