from django.shortcuts import render, get_object_or_404
from .models import Job

def list_jobs(request):
    context = {
        "page_title": "Lista de Vagas", 
        "jobs": Job.objects.all()
    }
    
    return render(request, "jobs/list.html", context)

def detail_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    context = {
        "page_title": job.title,
        "job": job
    }
    
    return render(request, "jobs/details.html", context)