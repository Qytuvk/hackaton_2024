from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    return render(request, 'Project_hakaton/main.html')

def register(request) -> HttpResponse:
    return render(request, "Project_hakaton/entry.html")

