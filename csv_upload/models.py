from django.db import models


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False, unique=True)
