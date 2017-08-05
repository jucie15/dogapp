from django.db import models
import os
from uuid import uuid4

class Profile(models.Model):
    upload_image = models.ImageField(upload_to='profile/')
    result1_name = models.CharField(max_length=128)
    result2_name = models.CharField(max_length=128)
    result3_name = models.CharField(max_length=128)
    result1_value = models.IntegerField(default=0)
    result2_value = models.IntegerField(default=0)
    result3_value = models.IntegerField(default=0)

    def __str__(self):
        return self.pk
