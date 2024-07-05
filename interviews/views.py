from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import Job
from .models import Chat

def create(request, job_pk):
    if request.method == "POST":
        job = get_object_or_404(Job, pk=job_pk)
        chat = Chat.objects.create(job=job)
        
        return redirect("interviews:details", uuid=chat.uuid)
    
    return HttpResponseNotAllowed(permitted_methods=("POST", ))

def details(request, uuid):
    chat = get_object_or_404(Chat, uuid=uuid)
    
    context = {
        "page_title": f"Entrevista: {chat.job.title}",
        "chat": chat,
    }
    return render (request, "interviews/details.html", context)
