from django.contrib import admin

# Register your models here.
from .models import Movie_Model

admin.site.register(Movie_Model)