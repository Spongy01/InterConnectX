from django.db import models

# Create your models here.

PROTOCOLS = [
    "REST",
    "SOAP",
    "GRAPHQL",
]


class Protocol_Relation(models.Model):
    caller_id = models.CharField(max_length=100, primary_key=True)
    protocol = models.CharField(max_length=7)
    caller_url = models.CharField(max_length=200)
    middleware_key = models.CharField(max_length=100, unique=True)
