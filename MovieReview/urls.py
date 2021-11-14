from django.urls import path
from .views import *

app_name='moviereview'

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('AddPost',AddPost.as_view(),name="addpost"),
    path('ViewPost/<int:pk>',ViewPost.as_view(),name='viewpost'),
    path('MyPost/<str:username>',MyPost.as_view(),name='mypost'),
    path('UserPost/<str:username>',UserPost.as_view(),name='userpost'),
    path('Director/<str:dir>',Director,name='director'),
]
