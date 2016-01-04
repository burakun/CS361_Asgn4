from django import forms
from odev4.models import Teacher
from django.db import models

class TeacherForm(forms.Form):
    first_name=forms.CharField(max_length=10)
    last_name=forms.CharField(max_length=10)
    office_details=forms.CharField(max_length=10)
    phone=forms.CharField(max_length=11)
    email_t=forms.EmailField()
    def __unicode__(self):
        return self.first_name

class StudentForm(forms.Form):
    firstt_name=forms.CharField(max_length=10)
    last_name=forms.CharField(max_length=10)
    email_s=forms.EmailField()
    def __unicode__(self):
        return self.firstt_name

class CourseForm(forms.Form):
    name=forms.CharField(max_length=20)
    code=forms.CharField(max_length=10)
    classroom=forms.CharField(max_length=5)
    times=forms.CharField()
    def __unicode__(self):
        return self.name