

from django.urls import path, include
from . import views

urlpatterns = [
    path("call/", views.api_call, name="API CALL"),

]
