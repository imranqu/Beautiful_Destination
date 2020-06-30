from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.
class register(CreateView):
    form_class=RegisterForm
    template_name='register.html'
    success_url=reverse_lazy('login')

