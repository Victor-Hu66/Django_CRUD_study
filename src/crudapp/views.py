from django.shortcuts import render
from django.http import HttpResponse



def home_view(request):
    return HttpResponse("<h1> Welcome Home Page<h1>")


