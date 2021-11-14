from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Movie_Review(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
    posted_on = models.DateTimeField(default=timezone.now)
    review = models.TextField()
    poster = models.ImageField()

    class Meta:
        ordering=['-posted_on']
    
    def get_absolute_url(self):
        return reverse("viewpost", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
