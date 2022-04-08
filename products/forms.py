from crispy_forms.layout import Submit
from django import forms
from django.forms import IntegerField, CharField

from products.models import Prodotti, Categoria
from crispy_forms.helper import FormHelper

class ProdottiForm(forms.ModelForm):

    helper = FormHelper() #inizializzo un nuovo attributo che inizializza form helper.
    helper.form_id = 'products_crispy_form'
    helper.form_method = 'POST' #questo perchè poi oglio evitare di scrivere i form nell'html con {% crispy %}
    helper.add_input(Submit('submit','Submit'))
    helper.inputs[0].field_classes = 'btn btn-success'

    class Meta:
        model = Prodotti
        #Nelle sllide abbiamo visto mettere le tuple mentre poi a lezione usiamo le liste
        #La situazione è la stessa  e non cambia nulla. Si usa la tupla per evitare i
        # duplicati dello stesso campo
        fields = ['owner','categoria' ,'name', 'dimensione','tipo_materiale', 'price', 'image']



class SearchForm(forms.Form):
    nome = CharField(max_length=255)
    min_price = IntegerField(required=False, min_value=0)
    max_price = IntegerField(required=False, min_value=0)