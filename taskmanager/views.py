from django.shortcuts import render_to_response
from django.template import RequestContext
import forms
import models

def index(request):
    if request.method == "POST":
        form = forms.AddForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.AddForm()

    tasks = models.Task.objects.filter(is_finished=False).all()
    return render_to_response('taskmanager/index.html', {
        "form": form,
        "tasks": tasks
    }, context_instance=RequestContext(request))
