from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Employee  # ✅ استخدم Employee بدل Info


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter password'
        })
    )


class CreateEmployeeForm(forms.ModelForm):  # ✅ غيرت الاسم ليعبر عن Employee
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'weight', 'height', 'salary', 'address', 'departments']
        widgets = {
            'departments': forms.CheckboxSelectMultiple(),  # لأن ده ManyToMany
        }


class UpdateEmployeeForm(forms.ModelForm):  # ✅ تعديل فورم التحديث
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'weight', 'height', 'salary', 'address', 'departments']
        widgets = {
            'departments': forms.CheckboxSelectMultiple(),
        }
