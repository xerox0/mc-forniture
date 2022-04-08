import datetime
import os
import random

from django.db import models
from user_manage.models import User,Owner,Cliente
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext (filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )



class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False,blank=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.nome


class Prodotti(models.Model):

    #definisco attributi che poi diventeranno colonne della mia tabella
    #grazie al concetto delle migration posso fare delle migrazioni e applicarle al mio db
    #La chiave di default la mette Django con un ID incrementale

    owner = models.ForeignKey(Owner, related_name='prodotti', on_delete=models.PROTECT)# proteggo gli al tri post dello stesso fornitore , mentre in Fornitore ho messo il CAscade perchè se cancelllo l'autore deve perdersi ogni suo prodotto
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    #la related name la uso qui per fare subito delle operazioni sul DB

    name = models.CharField(max_length=255)

    dimensione = models.CharField(max_length=255, default=None)
    tipo_materiale = models.CharField(max_length=255,default=None)
    price = models.CharField(max_length=255)
    review = models.TextField(default='Hello')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


    #c'è la possibilità di andare a sovrascrivere alcune funzioni in base.py
    def __str__(self):
        return f'{self.owner} - id: {self.id}'




