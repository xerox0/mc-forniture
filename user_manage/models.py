from django.db import models
from django.contrib.auth.models import AbstractUser,User

class User(AbstractUser):
    is_owner = models.BooleanField('owne status',default=False)
    is_client = models.BooleanField('client status',default=False)

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='proprietario')

    #proprietario_id = models.CharField(max_length=255,default=None)
    #nome = models.CharField(max_length=255,default=None)
    #cognome = models.CharField(max_length=255,default=None)
    #email = models.EmailField(max_length=254,default='000000')

    def __str__(self):
        return self.user.username

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='cliente')
    #cliente_id = models.CharField(max_length=255,default=None)
    #nome = models.CharField(max_length=255,default=None)
    #cognome = models.CharField(max_length=255,default=None)
    #email = models.EmailField(max_length=254,default=None)

    def __str__(self):
        return self.user.username