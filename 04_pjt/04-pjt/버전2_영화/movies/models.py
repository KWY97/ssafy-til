from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)