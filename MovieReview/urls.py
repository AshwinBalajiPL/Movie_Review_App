from django.urls import path
from .views import *

app_name='moviereview'

urlpatterns = [
    path('Home',Home.as_view(),name="home"),
]
