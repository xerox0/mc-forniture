from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from products.models import Prodotti


class ProdottiList(ListView):
    model = Prodotti
    template_name = 'products/list.html'

class ProdottiDetail(DetailView):
    model = Prodotti
    template_name = 'products/products_detail.html'

class ProdottiCreate(CreateView):
    model = Prodotti
