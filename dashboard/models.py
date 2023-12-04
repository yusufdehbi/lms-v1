from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractUser):
    USER = (
        (1, 'Admin'),
        (2, ''),
        (3, 'Employee'),
    )

    user_type = models.CharField(choices=USER, max_length=1)
    profile_pic = models.ImageField(upload_to='profile_picture/')
    tel = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    date_joined = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LeavePolicy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    maxAllowed = models.IntegerField(null=True)


class Status(models.Model):
    STATUS = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
        (3, 'Finished'),
    )
    name = models.CharField(choices=STATUS, max_length=1, default=1)


class LeveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leavePolicy = models.ForeignKey(LeavePolicy, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    @property
    def leaveDays(self):
        return self.end_date - self.start_date


class EmployeeLeaveBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
