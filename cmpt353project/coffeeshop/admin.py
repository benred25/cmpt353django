from django.contrib import admin

from .models import Item, Order

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'price']
    list_display = ('name', 'price')


class OrderAdmin(admin.ModelAdmin):
    fields = ['is_complete'] # editable fields by admin
    list_display = ('id', 'price', 'ordered_at', 'is_complete', 'ordered_items') # what to show the admin
    sortable_by = ('ordered_at', 'price', 'id', 'is_complete') # how the admin can sort the orders



admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
