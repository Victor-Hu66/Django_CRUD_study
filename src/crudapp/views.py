from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def home_view(request):
    return HttpResponse("<h1> Welcome Home Page<h1>")


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form' : form
    }
    return render(request, "crudapp/student_add.html", context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render( request , "crudapp/student_list.html", context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student' : student
    }
    return render(request, "crudapp/student_detail.html", context)

def student_delete (request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect("list")
    return render(request, 'crudapp/student_delete.html')

def student_update(request, id):
    student = get_object_or_404(Student, id=id) 
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'student' : student,
        'form' : form
    }
    
    return render(request, "crudapp/student_update.html", context)