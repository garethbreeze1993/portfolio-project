from django.shortcuts import render, get_object_or_404
import datetime
from .models import Job, Job_Post 


def home(request):
    jobs = Job.objects # this will get all our objects from the job database.
    return render(request, 'jobs/home.html', {'jobs':jobs})
	
def jobs_specific(request,job_id):
    detailjob = get_object_or_404(Job, pk=job_id) # uses primary key to search database. We get job_id got from urls.py
    return render(request,'jobs/detail.html',{'detailjob':detailjob})	

# Create your views here.
