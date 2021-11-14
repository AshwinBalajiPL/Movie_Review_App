from django import forms
from .models import  Movie_Review
from django.contrib.auth.models import User

class Review(forms.ModelForm):
    class Meta:
        model = Movie_Review
        fields = ['title','posted_by','director','review','poster']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'posted_by' : forms.TextInput(attrs={'class':'form-control','id':'posted_by','value':'','type':'hidden'}),
            'director' : forms.TextInput(attrs={'class':'form-control'}),        
            'review' : forms.Textarea(attrs={'class':'form-control'}),
        }
    