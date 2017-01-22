from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Department(models.Model):
    title = models.CharField(max_length=50)


class Course(models.Model):
    department = models .ForeignKey(Department, null=True)
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class UserEnrollment(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)


class UserLog(models.Model):
    user = models.ForeignKey(User)
    action_date_time = models.DateTimeField(default = datetime.now)
    action_title = models.CharField(max_length=400, default='')
