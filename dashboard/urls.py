from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('starter', views.starter_view),
    path('test', views.test_view, name='test'),
    # urls for admin

    # -> dashboard
    path('admin-dashboard', views.admin_dashboard_view),

    # -> employee management
    path('employee-management', views.employee_management_view, name="employee-management"),
    path('add-employee/', views.add_employee_view, name='add-employee'),

    # -> requests management
    path('request-management', views.request_management, name='request-management'),
    
    # -> leaves policies management
    path('leave-type-management', views.leave_type_management_view, name='leave-type-management'),
    path('add-leave-type', views.add_leave_type_view, name='add-leave-type'),
]
