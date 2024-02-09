from django.db import models

# Create your models here.
class entrepreneur(models.Model):
  name= models.CharField(max_length=100, verbose_name='Entrepreneur Name')
  email=models.EmailField(max_length=277, verbose_name='Email')

  def __str__(self):
    return str(self.id)