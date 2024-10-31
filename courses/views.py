from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from users.models import *

@login_required
def create_course(request):
    if request.method == 'POST':
        # Pass request.FILES to handle file uploads (for course_image)
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the course directly from the form
            course = form.save()

            # Flash success message
            messages.success(request, 'Course created successfully!')
            return redirect('Course:create_course')  # Redirect to a course list or another relevant page
        else:
            messages.error(request, 'Error creating the course. Please correct the form errors.')
    else:
        form = CourseForm()

    return render(request, 'courses/course_form.html', {'form': form, 'title': 'Create Course'})

def list_courses(request):
    # Fetch all available courses
    courses = Course.objects.all()

    # Render the courses in a template
    return render(request, 'courses/list_courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def update_course(request, course_id):
    pass

@login_required
def delete_course(request, course_id):
    pass


@login_required
def student_courses(request):
    student = request.user.student  # Assuming you have a OneToOne relationship between User and Student
    courses = student.courses.all()  # Fetching all courses registered by the student
    return render(request, 'courses/student_courses.html', {'courses': courses})

@login_required
def available_courses(request):
    student = request.user.student
    registered_courses = student.courses.all()
    available_courses = Course.objects.exclude(id__in=registered_courses)

    return render(request, 'courses/available_courses.html', {'available_courses': available_courses})

@login_required
def register_course(request, course_id):
    student = request.user.student
    course = get_object_or_404(Course, id=course_id)
    student.courses.add(course)
    messages.success(request, f'You have successfully registered for {course.title}.')
    return redirect('Course:available_courses')


@login_required
def student_course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    student = request.user.student  # Assuming you have a student profile for each user
    context = {
        'course': course,
       
    }
    return render(request, 'courses/student-course_detail.html', context)




