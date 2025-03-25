from django.db import models
from django.db.utils import settings

from myshop.settings import STRIPE_SECRET_KEY

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length= 100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=200,blank = True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields = ['-created'])
        ]
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        # self.items -> Refers to OrderItem Model and .all() basically retrieves all the order item  related to that order
        # 1  <--->  Many
        return sum(item.get_cost() for item in self.items.all())
    def get_stripe_uri(self):
        if not self.stripe_id:
            return ''
        if '__test__' in settings.STRIPE_SECRET_KEY:
            path = "/test/"
        else:
            path = '/'
        return f"https://dashboard.stripe.com{path}payments/{self.stripe_id}"
        

class OrderItem(models.Model):
    orders = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'shop.Product',
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity
    
