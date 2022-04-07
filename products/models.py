from django.db import models
from user_manage.models import User,Owner,Cliente
# Create your models here.

class Prodotti(models.Model):

    #definisco attributi che poi diventeranno colonne della mia tabella
    #grazie al concetto delle migration posso fare delle migrazioni e applicarle al mio db
    #La chiave di default la mette Django con un ID incrementale

    owner = models.ForeignKey(Owner, related_name='prodotti', on_delete=models.PROTECT)# proteggo gli al tri post dello stesso fornitore , mentre in Fornitore ho messo il CAscade perchè se cancelllo l'autore deve perdersi ogni suo prodotto

    #la related name la uso qui per fare subito delle operazioni sul DB

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    review = models.TextField(default='Hello')
    image = models.ImageField(upload_to='img/', blank=True)


    #c'è la possibilità di andare a sovrascrivere alcune funzioni in base.py
    def __str__(self):
        return f'{self.owner} - id: {self.id}'