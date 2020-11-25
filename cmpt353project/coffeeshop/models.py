from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ForeignKey(Item, on_delete=models.PROTECT)
    price = models.FloatField()
    ordered_at = models.DateTimeField('order_timestamp')

    def __str__(self):
        return self.items
