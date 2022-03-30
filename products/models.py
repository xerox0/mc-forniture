from django.db import models

# Create your models here.

class Prodotti(models.Model):

    #definisco attributi che poi diventeranno colonne della mia tabella
    #grazie al concetto delle migration posso fare delle migrazioni e applicarle al mio db
    #La chiave di default la mette Django con un ID incrementale

    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.TextField()

    #c'è la possibilità di andare a sovrascrivere alcune funzioni in base.py
    def __str__(self):
        return f'{self.name} - id: {self.id}'