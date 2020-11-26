from django.db import models

# Create your models here.


class Item(models.Model):
    """
    An item model with a name and price
    """
    name = models.CharField(max_length=55)
    price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    """
    OrderItem model is for when the user adds an item to their order
    """
    name = models.CharField(max_length=55)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class CurrentOrderItem(models.Model):
    """
    CurrentOrderItem is the same as OrderItem but gets erased after each order is completed
    """
    name = models.CharField(max_length=55)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Order holds all the info of the users order like items, price, when they ordered, and if it's complete
    """
    items = models.ManyToManyField(OrderItem)
    price = models.FloatField()
    ordered_at = models.DateTimeField('Time Ordered')
    is_complete = models.BooleanField(default=False)

    def ordered_items(self):
        """
        used to display the orders to staff on the admin page
        """
        string = ""
        for item in self.items.all():
            string += str(item.quantity) + " " + str(item.name) + ", "
        return string

    def __str__(self):
        return "Order #"+str(self.id)

