from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Order, OrderItem
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse

# Create your views here.

def menu(request):
    item_list = Item.objects.all()
    order_list = Order.objects.all()
    context = {'item_list': item_list,
               'order_list': order_list}
    return render(request, 'coffeeshop/menu.html', context)

def order(request):
    print('order')
    if request.method == 'POST':
        item = Item.objects.get(name=request.POST.get('item'))

        context = {'item': item}
        return render(request, 'coffeeshop/order.html', context)

def confirm(request):
    print('confirm')
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        item = Item.objects.get(name=request.POST.get('name'))


    return HttpResponseRedirect(reverse('menu'))


