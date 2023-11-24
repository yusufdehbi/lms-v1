from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'index.html')

def starter_view(request):
    return render(request, 'starter.html')


def admin_dashboard_view(request):
    return render(request, 'admin dashboard.html')

def employee_management_view(request):
    return render(request, 'employee_management.html')

def request_management(request):
    return render(request, 'request_management.html')

def leave_type_management_view(request):
    return render(request,  'leave_type_management.html')

# def add_leave_type_view(request):
#     return render(request, 'add_leave_type.html')

def add_leave_type_view(request):
    return render(request, 'add_leave_type.html')

def add_employee_view(request):
    return render(request, 'add_employee.html')


def test_view(request):
    return render(request, 'test.html')