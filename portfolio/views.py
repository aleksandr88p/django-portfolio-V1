from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import random

def home(request):
    # return HttpResponse("THIS IS MY PORTFOLIO")
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects})