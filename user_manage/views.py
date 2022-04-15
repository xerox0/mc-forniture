from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user_manage.forms import OwnerSignUpForm, ClienteSignUpForm
from user_manage.models import User


class ClienteSignUpView(CreateView):
    model = User
    form_class = ClienteSignUpForm
    template_name = 'user_manage/registration/user_creation.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'cliente'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('homepage')

class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'user_manage/registration/owner_creation.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owne'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('homepage')





# def FornitoreCreation(request):
#     # form_class = FornitoreForm
#     if request.method == 'POST':
#         fornitore_form = FornitoreForm(request.POST)
#         user_gen = UserSingUpForm(request.POST)
#         if fornitore_form.is_valid() and user_gen.is_valid():
#             usr = user_gen.save(commit=False)
#             usr.is_client = True
#             usr = user_gen.save()
#             own = fornitore_form.save(commit=False)
#             own.owner_fornitore = usr
#             own.save()
#             login(request, usr)
#             return redirect('homepage')
#     else:
#         user_gen = UserSingUpForm()
#         fornitore_form = FornitoreForm()
#
#     return render(request, 'user_manage/registration/owner_creation.html',
#                   {'fornitore_form': fornitore_form, 'user_form': user_gen})
#     # template_name = 'user_manage/registration/owner_creation.html' #creo il templates che non sarà diverso dal templateform vecchi
#     # success_url =  reverse_lazy('homepage')
#
#
# def clientecreation(request):
#     if request.method == 'POST':
#         cliente_form = ClientForm(request.POST)
#         if cliente_form.is_valid():
#             cli = cliente_form.save(commit=False)
#             cli.is_cliente = True
#             cli = cliente_form.save()
#
#             login(request, cli)
#             redirect('homepage')
#     else:
#         cliente_form = ClientForm
#     return render(request, 'user_manage/registration/user_creation.html', {'form': cliente_form})
