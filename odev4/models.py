from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    office_details=models.CharField(max_length=10)
    phone=models.CharField(max_length=11)
    email_t=models.EmailField()
    def __unicode__(self):
        return self.first_name

class Student(models.Model):
    firstt_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email_s=models.EmailField()
    def __unicode__(self):
        return self.firstt_name

class Course(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=10)
    classroom=models.CharField(max_length=5)
    times=models.CharField(max_length=10)
    teacher=models.ForeignKey(Teacher, null=True)
    students=models.ManyToManyField(Student, null=True)
    def __unicode__(self):
        return self.name