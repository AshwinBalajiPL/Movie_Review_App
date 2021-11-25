from django.db import models
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Movie_Review
from django.views.generic import ListView,DetailView,CreateView
from .forms import Review
from django.core.paginator import Paginator

# Create your views here.
class Home(ListView):
    paginate_by = 5
    model = Movie_Review
    template_name= 'home.html'

class AddPost(CreateView):
    model = Movie_Review
    form_class = Review
    template_name = 'addpost.html'
    success_url = '/'

class ViewPost(DetailView):
    model = Movie_Review
    template_name = 'viewpost.html'

class MyPost(ListView):
    model = Movie_Review
    template_name = "mypost.html"
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Movie_Review.objects.filter(posted_by=user).order_by('-posted_on')

class UserPost(ListView):
    model = Movie_Review
    template_name = "userpost.html"
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Movie_Review.objects.filter(posted_by=user).order_by('-posted_on')

def Director(request,dir):
    directors= Movie_Review.objects.filter(director=dir)
    return render(request,'director.html',{'directors':dir,'directorposts':directors})
