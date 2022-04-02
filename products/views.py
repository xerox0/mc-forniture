from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from products.models import Prodotti
from products.forms import ProdottiForm

class ProdottiList(ListView):
    model = Prodotti
    template_name = 'products/list.html'

class ProdottiDetail(DetailView):
    model = Prodotti
    template_name = 'products/products_detail.html'

class ProdottiCreate(CreateView):
    model = Prodotti
    template_name = 'products/create.html'
    #fields = ['owner','name', 'description', 'price']
    success_url = reverse_lazy('prod:products-list')
    form_class = ProdottiForm

class ProdottiDelete(DeleteView):
    model= Prodotti
    template_name = 'products/delete.html'
    success_url = reverse_lazy('prod:products-list')

class ProdottiUpdate(UpdateView):
    model = Prodotti
    template_name = 'products/update.html'
    #fields = ['owner','name','description','price']
    success_url = reverse_lazy('prod:products-list')
    form_class = ProdottiForm