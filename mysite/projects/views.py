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
# Create your views here.

def project_create(request):
    projects = Project.get.all()
    return render(request, "projectslist.html", {'projects' : projects})

def projectslist(request):
    projects = Project.objects.all()
    return render(request, "projectslist.html", {'projects' : projects})
