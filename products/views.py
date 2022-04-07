from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib import messages
from user_manage.decorator import owner_required
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from products.models import Prodotti
from products.forms import ProdottiForm, SearchForm


class ProdottiList(ListView):
    model = Prodotti
    template_name = 'products/list.html'

class ProdottiDetail(DetailView):
    model = Prodotti
    template_name = 'products/products_detail.html'

@method_decorator([login_required, owner_required], name='dispatch')
class ProdottiCreate(LoginRequiredMixin,CreateView):
    model = Prodotti
    template_name = 'products/create.html'
    #fields = ['owne','name', 'description', 'price']
    success_url = reverse_lazy('prod:products-list')
    form_class = ProdottiForm

@method_decorator(property,name='dispatch')
@method_decorator([login_required, owner_required], name='dispatch')
class ProdottiDelete(LoginRequiredMixin,DeleteView):
    model= Prodotti
    template_name = 'products/delete.html'
    success_url = reverse_lazy('prod:products-list')


@method_decorator([login_required, owner_required], name='dispatch')
class ProdottiUpdate(LoginRequiredMixin,UpdateView):
    model = Prodotti
    template_name = 'products/update.html'
    #fields = ['owne','name','description','price']
    success_url = reverse_lazy('prod:products-list')
    form_class = ProdottiForm


    def form_valid(self, form):
        frm = form.save(commit=False)

        return super().form_valid(form)
# class SearchProd(ListView):
#
#     model = Prodotti
#     form_class = SearchForm
#     template_name = 'products/search.html'
#
#     def get_queryset(self):
#         nome = self.request.GET.get('nome')
#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')
#         if  nome:
#             if min_price:
#                 if max_price:
#                     srv = self.model.objects.filter(
#                                                     nome=nome, price__gte=min_price,
#                                                     price__lte=max_price).order_by('-price')
#                 else:
#                     srv = self.model.objects.filter(service__exact=selec_serv,
#                                                     luogo_identifier__city__exact=nome,
#                                                     price__gte=min_price).order_by('-price')
#             else:
#                 if max_price:
#                     srv = self.model.objects.filter(service__exact=selec_serv,
#                                                     luogo_identifier__city__exact=nome,
#                                                     price__lte=min_price, ).order_by('-price')
#                 else:
#                     srv = self.model.objects.filter(service__exact=selec_serv,
#                                                     luogo_identifier__city__exact=nome).order_by('-price')
#         else:
#             srv = self.model.objects.none()
#         return srv
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(SearchView, self).get_context_data(**kwargs)
#         # selec_serv = self.request.GET.get('servi')
#         context['form'] = SearchForm(initial={
#             'city': self.request.GET.get('city'),
#             'servi': self.request.GET.get('servi'),
#             'min_price': self.request.GET.get('min_price'),
#             'max_price': self.request.GET.get('max_price'),
#         })
#         return context
