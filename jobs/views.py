from django.shortcuts import render
import datetime


def home(request):
    #now = datetime.datetime.now()
    #current_year = now.year
    return render(request, 'jobs/home.html')

# Create your views here.
