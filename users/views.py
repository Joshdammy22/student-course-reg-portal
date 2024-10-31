from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from courses.models import *

# Student Registration View
def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            matric_number = form.cleaned_data['matric_number']
            last_name = form.cleaned_data['last_name']

            try:
                pre_existing_student = PreExistingStudent.objects.get(matric_number=matric_number, last_name=last_name)
                request.session['pre_existing_student_id'] = pre_existing_student.id
                # Add success message
                messages.success(request, 'Registration successful! Please set your password to complete the process.')
                return redirect('student_set_password')
            except PreExistingStudent.DoesNotExist:
                messages.error(request, 'Matric number or surname is incorrect.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = StudentRegisterForm()
    return render(request, 'users/student_register.html', {'form': form})

# Set Password for Student View
def student_set_password(request):
    if 'pre_existing_student_id' not in request.session:
        return redirect('student_register')

    pre_existing_student = PreExistingStudent.objects.get(id=request.session['pre_existing_student_id'])

    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                User = get_user_model()
                user = User.objects.create_user(
                    username=pre_existing_student.matric_number,
                    email=f"{pre_existing_student.matric_number}@university.com",
                    password=password1,
                    first_name=pre_existing_student.first_name,
                    last_name=pre_existing_student.last_name
                )
                Student.objects.create(
                    user=user,
                    matric_number=pre_existing_student.matric_number,
                    first_name=pre_existing_student.first_name,
                    last_name=pre_existing_student.last_name,
                    gender=pre_existing_student.gender
                )
                del request.session['pre_existing_student_id']
                # Add success message
                messages.success(request, 'Password set successfully! You can now log in.')
                return redirect('student_login')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = SetPasswordForm()

    return render(request, 'users/set_password.html', {'form': form})

# Student Login View
def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            matric_number = form.cleaned_data['matric_number']
            password = form.cleaned_data['password']
            try:
                user = Student.objects.get(matric_number=matric_number).user
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful! Welcome to your dashboard.')
                    return redirect('student_dashboard')
                else:
                    messages.error(request, 'Invalid login credentials.')
            except Student.DoesNotExist:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = StudentLoginForm()
    return render(request, 'users/student_login.html', {'form': form})



# Student Dashboard View
@login_required
def student_dashboard(request):
    student = request.user.student  # Assuming a OneToOne relationship between User and Student
    courses = student.courses.all()
    return render(request, 'users/student_dashboard.html', {
        'courses': courses,
    })
    


from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Add success message on logout
        messages.success(request, 'You have successfully logged out.')
        # Continue with the normal logout process
        return super().dispatch(request, *args, **kwargs)
