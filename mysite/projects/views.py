from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from .models import Choice, Question
from django.utils.decorators import method_decorator
from .models import Project
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
# Create your views here.

@login_required(login_url = "/login")
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        return HttpResponseRedirect(reverse("projects:projectslist"))


    #if request.method == "POST":
    #    print (request.POST.get("Title"))
    #    print (request.POST.get("description"))

    context = {
        "form": form,
    }
    return render(request, "project_form.html", context)
    
@login_required(login_url = "/login")
def projectslist(request):
    projects = Project.objects.all()
    context = {
        "objects_list": projects,
        "title": "List"
    }
    return render(request, "projectslist.html", context)
