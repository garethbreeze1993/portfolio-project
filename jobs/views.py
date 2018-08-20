from django.shortcuts import render
import datetime
from .models import Job 


def home(request):
    jobs = Job.objects # this will get all our objects from the job database.
    return render(request, 'jobs/home.html', {'jobs':jobs})

# Create your views here.
