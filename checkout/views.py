from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cart.models import Cart
from checkout.forms import OrderCreateForm
from checkout.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            return render (request,'checkout/completato.html',{'order':order})

    else:
            form= OrderCreateForm
    return render(request,'checkout/create.html',{'cart':cart,'form':form})