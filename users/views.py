from django.shortcuts import render,redirect
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import *


class UserRegistration(CreateView):
    form_class = Userregister
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')