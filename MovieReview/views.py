from django.db import models
from django.shortcuts import render
from .models import Movie_Review
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
class Home(ListView):
    model = Movie_Review
    template_name= 'home.html'

