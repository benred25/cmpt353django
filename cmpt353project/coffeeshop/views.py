from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Order, OrderItem, CurrentOrderItem
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse
import datetime

# Create your views here.


def menu(request):
    print('menu')
    item_list = Item.objects.all()
    order_list = Order.objects.all()
    current_order = CurrentOrderItem.objects.all()
    latest_order = Order.objects.filter().order_by('-id')[0]
    context = {'item_list': item_list,
               'order_list': order_list,
               'current_order': current_order,
               'latest_order': latest_order}
    return render(request, 'coffeeshop/menu.html', context)


def order(request):
    print('order')
    if request.method == 'POST':
        item = Item.objects.get(name=request.POST.get('item'))
        quantity = request.POST.get('quantity')

        # create item to add to just current order for display purposes
        cur_order_item = CurrentOrderItem()
        cur_order_item.name = item.name
        cur_order_item.price = item.price * float(quantity)
        cur_order_item.quantity = quantity
        cur_order_item.save()

    return HttpResponseRedirect(reverse('menu'))


def complete(request):
    order_to_add = Order.objects.create(price=0.0, ordered_at=datetime.datetime.now())
    total_price = 0.0
    for item in CurrentOrderItem.objects.all():
        order_to_add.items.create(name=item.name, price=item.price, quantity=item.quantity)

        total_price += item.price

    order_to_add.price = total_price
    order_to_add.save()

    for item in order_to_add.items.all():
        print(item.name)

    CurrentOrderItem.objects.all().delete()

    return HttpResponseRedirect(reverse('menu'))


