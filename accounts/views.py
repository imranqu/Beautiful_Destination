from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.
class register(CreateView):
    print(RegisterForm)
    form_class=RegisterForm
    success_url=reverse_lazy('login')
    template_name='register.html'
