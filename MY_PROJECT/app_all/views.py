from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
import logging

from .forms import *
from .models import Employee

logger = logging.getLogger(__name__)


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login_page')
    else:
        form = CustomUserCreationForm()

    return render(request, 'web/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard_page')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'web/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login_page')


def landing_page(request):
    return render(request, 'app_all/new_landing.html')  # ← ملف HTML جديد هنعمله



@login_required(login_url='login_page')
def dashboard_page(request):
    all_employees = Employee.objects.all()
    return render(request, 'web/dashboard.html', {'employees': all_employees})


@login_required(login_url='login_page')
def create_employee(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully.')
            return redirect('dashboard_page')
    else:
        form = CreateEmployeeForm()

    return render(request, 'web/create-employee.html', {'form': form})


@login_required(login_url='login_page')
def view_employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'web/employee.html', {'employee': employee})


@login_required(login_url='login_page')
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('dashboard_page')
    else:
        form = UpdateEmployeeForm(instance=employee)

    return render(request, 'web/update.html', {'form': form, 'employee': employee})


@login_required(login_url='login_page')
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('dashboard_page')


@login_required(login_url='login_page')
def search_employee(request):
    query = request.GET.get('q')
    results = []

    try:
        if query:
            filters = Q(first_name__icontains=query) | Q(last_name__icontains=query)
            try:
                id_query = int(query)
                filters |= Q(id=id_query)
            except ValueError:
                pass

            results = Employee.objects.filter(filters)
    except Exception as e:
        logger.error("Search error: %s", e)

    return render(request, 'web/search.html', {'results': results, 'query': query})


def error_404_view(request, exception):
    return render(request, 'web/404.html', status=404)
