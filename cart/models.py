from django.db import models
from book.models import Book
from user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    STATUS_CHOICES = [
        ('unordered', 'Unordered'),
        ('ordered', 'Ordered'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='unordered', max_length=20)


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    # def _str_(self):
    #     return f"{self.quantity} x {self.book.title} in cart for {self.cart.user.username}"