from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.contrib import messages
from user_manage.decorator import owner_required
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from products.models import Prodotti, Categoria, Review
from products.forms import ProdottiForm, ReviewForm, SearchForm

def CategoriaView(request):
    category = request.GET.get('category')

    products = Prodotti.objects.filter(categoria__nome=category)

    categories = Categoria.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/categoria.html', context)

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
    success_url = reverse_lazy('homepage')
    form_class = ProdottiForm


@method_decorator([login_required, owner_required], name='dispatch')
class ProdottiDelete(LoginRequiredMixin,DeleteView):
    model= Prodotti
    template_name = 'products/delete.html'
    success_url = reverse_lazy('homepage')


@method_decorator([login_required, owner_required], name='dispatch')
class ProdottiUpdate(LoginRequiredMixin,UpdateView):
    model = Prodotti
    template_name = 'products/update.html'
    #fields = ['owne','name','description','price']
    success_url = reverse_lazy('prod:products-category')
    form_class = ProdottiForm


    def form_valid(self, form):
        frm = form.save(commit=False)

        return super().form_valid(form)

class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    template_name = 'products/recensioni.html'
    success_url = reverse_lazy('prod:products-category')
    form_class = ReviewForm

    def add_comment(request, pk):
        eachProduct = Prodotti.objects.get(id=pk)

        form = ReviewForm(instance=eachProduct)

        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=eachProduct)
            if form.is_valid():
                name = request.user.username
                body = form.cleaned_data['comment_body']
                rate_forn = form.full_clean['rating_fornitore']
                rate_prod = form.full_clean['rating_prodotto']
                c = Review(prodotto=eachProduct, comment_name=name, comment_body=body,rating_fornitore=rate_forn,rating_prodotto=rate_prod)
                c.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect('prod:products-category')
            else:
                print('form is invalid')
        else:
            form = ReviewForm()

        context = {
            'form': form
        }

        return render(request, 'products/recensioni.html', context)

class SearchView(ListView):
    model = Prodotti
    form_class = SearchForm
    template_name = "products/search2.html"
    context_object_name = 'search_list'
    success_url = reverse_lazy('prod:products-category')
    def get_queryset(self):


            nome= self.request.GET.get('nome')
            material=self.request.GET.get('material')
            min_price = self.request.GET.get('min_price')
            max_price = self.request.GET.get('max_price')
            if nome and material:
                        if min_price:
                             if max_price:
                                        qs = self.model.objects.filter(name__icontains=nome,tipo_materiale__icontains=material,price__gte=min_price,price__lte=max_price).order_by('-price')
                             else:
                                    qs = self.model.objects.filter(name__icontains=nome,tipo_materiale__icontains=material ,price__gte=min_price).order_by('-price')
                        else:
                                 if max_price:
                                             qs = self.model.objects.filter(name__icontains=nome,tipo_materiale__icontains=material).order_by('-price')
            else:
                 qs= self.model.objects.none()
            return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView,self).get_context_data(**kwargs)
        context['form'] = SearchForm(initial= {
            'nome': self.request.GET.get('nome'),
            'material': self.request.GET.get('material'),
            'min_price': self.request.GET.get('min_price'),
            'max_price': self.request.GET.get('max_price'),
        })
        return context


# def searchBar(request):
#     if request.method == 'GET':
#
#         query = request.GET.get('query')
#
#         if query:
#             products = Prodotti.objects.filter(name__icontains=query)
#             return render(request, 'products/search2.html', {'products':products})
#
#         else:
#             print("No information to show")
#             return render(request, 'products/search2.html', {})
#
