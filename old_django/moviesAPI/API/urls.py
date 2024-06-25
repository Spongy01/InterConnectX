from django.urls import path
from . import views


urlpatterns = [
    path("movies/<int:id>", views.get_movie, name="get movie"),
]
