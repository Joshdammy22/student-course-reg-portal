from django import forms
from .models import *

# Mixin for adding Bootstrap classes to non-model forms
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# Mixin for adding Bootstrap classes to model forms
class BootstrapModelFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class StudentRegisterForm(BootstrapModelFormMixin):
    class Meta:
        model = Student
        fields = ['last_name', 'matric_number']
        widgets = {
            'matric_number': forms.TextInput(attrs={'placeholder': 'Matric Number'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        error_messages = {
            'matric_number': {
                'unique': 'Student with this Matric number already exists.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        matric_number = cleaned_data.get('matric_number')
        last_name = cleaned_data.get('last_name')

        if matric_number and last_name:
            try:
                pre_existing_student = PreExistingStudent.objects.get(matric_number=matric_number, last_name=last_name)
            except PreExistingStudent.DoesNotExist:
                self.add_error('matric_number', 'Matric number or surname is incorrect.')
        return cleaned_data

class SetPasswordForm(BootstrapFormMixin, forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

class StudentLoginForm(BootstrapFormMixin, forms.Form):
    matric_number = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': 'Matric Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
