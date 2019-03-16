from django.db import models

# Create your models here.

class Scraper_data(models.Model):

    urls = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)