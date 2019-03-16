from django.db import models


class ScraperData(models.Model):


    url = models.CharField(max_length=500, null=True, blank=True)
    domain = models.CharField(max_length=50, null=True, blank=True)
    is_processing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
