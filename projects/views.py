# This file connect data base to the front end. 
# Send data from database to HTML templates

from django.shortcuts import render
from projects.models import Project # importing database model in models.py

# Create your views here.
def project_index(request):
    projects = Project.objects.all() # Retrieve all objects in projects table
    context = { # for rendering view
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# pk = primary key
def project_detail(request, pk):
    project = Project.objects.get(pk=pk) # get proj with pk = to that in the arg.
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

