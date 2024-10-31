# users/urls.py
from django.urls import path
from .views import *
from .views import CustomLogoutView

urlpatterns = [
    # Authentication and Registration URLs
    path('student/register/', student_register, name='student_register'),
    path('student/set-password/', student_set_password, name='student_set_password'),
    path('student/login/', student_login, name='student_login'),
    path('logout/', CustomLogoutView.as_view(next_page='home'), name='logout'),

    # Dashboard URLs
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
]
