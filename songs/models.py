from django.db import models

# Create your models here.

class Song(models.Model):
  name = models.CharField(max_length=100)
  song = models.FileField(upload_to='songs')

  def __str__(self):
    return self.name