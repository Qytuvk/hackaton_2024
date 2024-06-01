from django.http import HttpResponse
from django.shortcuts import render
import our_parser1
from app.models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def index(request) -> HttpResponse:
    data = Profile.objects.all()
    return render(request, 'Project_hakaton/main.html', {'data': data})

def register(request) -> HttpResponse:
    return render(request, "Project_hakaton/entry.html")


@csrf_exempt
def upload_file(request):
    file = request.GET['file']
    if file is not None:
        our_parser1.set_file_path(file)
    else:
        print("нет")
    return render(request, "Project_hakaton/main.html")