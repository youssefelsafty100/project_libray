# app_all/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.user_register, name='register_page'),
    path('login/', views.user_login, name='login_page'),
    path('logout/', views.user_logout, name='logout_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),

    # CRUD - Employees
    path('create/', views.create_employee, name='create_info'),
    path('info/<int:employee_id>/', views.view_employee_details, name='view_info_details'),
    path('update/<int:employee_id>/', views.update_employee, name='update_info'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_info'),

    # Search
    path('search/', views.search_employee, name='search_info'),
]
