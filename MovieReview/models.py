from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Movie_Review(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
    posted_on = models.DateTimeField(default=timezone.now)
    review = models.TextField()
    poster = models.ImageField()


    def __str__(self):
        return self.title
