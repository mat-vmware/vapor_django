from django.db import models

class VCenter(models.Model):
    address = models.CharField(max_length=64)
    port = models.IntegerField(default=0) 
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    uuid = models.CharField(max_length=64)
