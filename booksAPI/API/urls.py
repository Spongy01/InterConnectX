from django.urls import path
from . import views


urlpatterns = [
    path("books/<int:isbn>", views.get_book, name="get book"),
]