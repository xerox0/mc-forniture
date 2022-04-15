from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView

from forum.forms import ForumForm, RispostaForm
from forum.models import Forum, Risposta
from user_manage.decorator import  client_required
from user_manage.models import Cliente


class ThreadList(ListView):
    model = Forum
    template_name = 'forum/lista_thread.html'
    context_object_name = 'lista_thread'



class RispostaList(ListView):
    model = Risposta
    template_name = 'forum/discussione.html'
    context_object_name = 'lista_commenti'


class ThreadCreate(LoginRequiredMixin,CreateView):
    model = Forum
    form_class = ForumForm
    template_name = 'forum/crea_thread.html'
    success_url = reverse_lazy('forum:thread-list')
    def form_valid(self, form):
        form.instance.user = Cliente.objects.get(user__username=self.request.user.username)
        return super(ThreadCreate,self).form_valid(form)

@method_decorator([login_required, client_required], name='dispatch')
class RispostaCreate(CreateView):
    model = Risposta
    form_class = RispostaForm
    template_name = 'forum/crea_risposta.html'
    success_url = reverse_lazy('forum:thread-list')
    def form_valid(self, form):
        form.instance.user = Cliente.objects.get(user__username=self.request.user.username)
        return super(RispostaCreate,self).form_valid(form)

