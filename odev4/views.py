from django.shortcuts import render
from django.shortcuts import render_to_response
from odev4.forms import TeacherForm, StudentForm, CourseForm
from odev4.models import Teacher, Student, Course
from django.http import HttpResponseRedirect
from django.shortcuts import RequestContext
# Create your views here.
def addteacher(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            a=Teacher(first_name=form.cleaned_data["first_name"],last_name=form.cleaned_data["last_name"],
                      office_details=form.cleaned_data["office_details"],phone=form.cleaned_data["phone"],email_t=form.cleaned_data["email_t"])
            a.save()
            return HttpResponseRedirect('all-teachers/')
    else:
        form=TeacherForm()
    return render_to_response('add_teacher.html',{'form':form},RequestContext(request))

def allteachers(request):
    return render_to_response('all_teachers.html',{'teacher_list': Teacher.objects.all()})

def addstudent(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            a=Student(firstt_name=form.cleaned_data["firstt_name"],last_name=form.cleaned_data["last_name"],
                      email_s=form.cleaned_data["email_s"])
            a.save()
            return HttpResponseRedirect('all-students/')
    else:
        form=StudentForm()
    return render_to_response('add_student.html',{'form':form},RequestContext(request))

def allstudents(request):
    return render_to_response('all_students.html',{'student_list': Student.objects.all()})

def addcourse(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            c=Course(name=form.cleaned_data["name"],code=form.cleaned_data["code"],
                      classroom=form.cleaned_data["classroom"],times=form.cleaned_data["times"])
            c.save()
            return HttpResponseRedirect('all-courses/')
    else:
        form=CourseForm()
    return render_to_response('add_course.html',{'form':form},RequestContext(request))

def allcourses(request):
    return render_to_response('all_courses.html',{'course_list': Course.objects.all()})