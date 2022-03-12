from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField

# Create your models here.

class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    nome = models.TextField()
    cognome = models.TextField()
    sesso = models.TextField()
    bambino_di_merda = models.BooleanField()



