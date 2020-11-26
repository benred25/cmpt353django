from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class CurrentOrderItem(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    price = models.FloatField()
    ordered_at = models.DateTimeField('order_timestamp')
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return "Order #"+str(self.id)

