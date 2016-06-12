from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from .models import Choice, Question
from django.views import generic
from django.utils import timezone
from django.utils.decorators import method_decorator
from .models import Project
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
# Create your views here.

def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save

    #if request.method == "POST":
    #    print (request.POST.get("Title"))
    #    print (request.POST.get("description"))

    context = {
        "form": form,
    }
    return render(request, "project_form.html", context)

def projectslist(request):
    projects = Project.objects.all()
    context = {
        "objects_list": projects,
        "title": "List"
    }
    return render(request, "projectslist.html", context)
