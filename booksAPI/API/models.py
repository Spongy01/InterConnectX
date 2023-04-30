from django.db import models

# Create your models here.
class CustomBookManager(models.Manager):
    def select_columns(self, columns):
        return self.get_queryset().only(*columns)

class Book_Model(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, primary_key=True)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField()
    language = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    objects = CustomBookManager()

    def __str__(self):
        return self.title
