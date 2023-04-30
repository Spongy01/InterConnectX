from django.contrib import admin

# Register your models here.
from .models import Clients, ClientData

admin.site.register(Clients)
admin.site.register(ClientData)