from django.shortcuts import reverse
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

    def save_profile(self, dog_name, dog_value):
        self.result1_name, self.result1_value = dog_name[0], dog_value[0]*100
        self.result2_name, self.result2_value = dog_name[1], dog_value[1]*100
        self.result3_name, self.result3_value = dog_name[2], dog_value[2]*100
        self.save()

    def get_absolute_url(self):
        return reverse('matching:result', args=[self.pk])
