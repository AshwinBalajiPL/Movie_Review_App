from django.contrib import admin
from MovieReview import models
# Register your models here.
class Movie_Review_Admin(admin.ModelAdmin):
    list_display = ('title','posted_by','posted_on')
admin.site.register(models.Movie_Review, Movie_Review_Admin)
