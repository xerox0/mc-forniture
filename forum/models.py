from django.db import models

# Create your models here.
from user_manage.models import Owner, Cliente,User


class Forum(models.Model):

    user = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    titolo =  models.CharField(max_length=255,)
    descrizione = models.CharField(max_length=255,)
    contenuto =  models.CharField(max_length=255)

    def __str__(self):
        return f'{self.titolo}'
class Risposta(models.Model):
    user = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    commento =models.CharField(max_length=255)

    def __str__(self):
        return  f'{self.commento}'
