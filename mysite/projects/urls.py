from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'projects'
urlpatterns = [
    url(r'^$', views.projectslist, name="projectslist"),
]
