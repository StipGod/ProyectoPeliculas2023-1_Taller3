from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Anime/images/')
    url = models.URLField(blank=True)
