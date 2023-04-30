from django.db import models

# Create your models here.


class CustomMovieManager(models.Manager):
    def select_columns(self, columns):
        return self.get_queryset().only(*columns)


class Movie_Model(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    director = models.CharField(max_length=255)
    actors = models.TextField()
    genre = models.CharField(max_length=255)
    rating = models.CharField(max_length=10)
    runtime = models.IntegerField()
    id = models.AutoField(primary_key=True)

    objects = CustomMovieManager()
