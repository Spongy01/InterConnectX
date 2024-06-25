from django.contrib import admin

# Register your models here.
from .models import Book_Model

admin.site.register(Book_Model)