from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    image = models.ImageField()
    def __str__(self):
        return self.name
    def static_name(self):
        return "master/images/"+self.image.name[8:]

class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to="testimonial_pics")
    def __str__(self):
        return self.title

# Create your models here.
