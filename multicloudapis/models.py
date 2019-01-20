# Create your models here.

from django.db import models


class CloudFileSystem(models.Model):
    name = models.CharField(max_length=100000,blank=True,default='ram')
    aws_count = models.IntegerField(max_length=100000, blank=True, default=0)
    azure_count = models.IntegerField(max_length=100000, blank=True, default=0)
    gcp_count = models.IntegerField(max_length=100000, blank=True, default=0)
