from django.contrib import admin
from MovieReview import models
# Register your models here.
class Movie_Review_Admin(admin.ModelAdmin):
    list_view = ('title','posted_on')
admin.site.register(models.Movie_Review, Movie_Review_Admin)
