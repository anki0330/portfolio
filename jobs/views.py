from django.shortcuts import render
from .models import job

def home(request):
    Job = job.objects
    return render(request,'jobs/home.html',{"Job":Job})
def app(request):
    return render(request,'jobs/app.html')
