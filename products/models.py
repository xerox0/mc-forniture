from django.db import models

# Create your models here.
class Prodotti(models.Model):
    #definisco attributi che poi diventeranno colonne della mia tabella
    #grazie al concetto delle migration posso fare delle migrazioni e applicarle al mio db
    owner = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.TextField()
