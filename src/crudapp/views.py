from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm


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

