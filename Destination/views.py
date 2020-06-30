from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


# Create your views here.
 
class index(TemplateView):
    template_name="index.html"