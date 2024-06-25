from django.db import models

# Create your models here.


class Clients(models.Model):
    client_id = models.CharField(max_length=100, primary_key=True)
    key = models.CharField(max_length=100, unique=True)


class ClientData(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    data = models.JSONField()
