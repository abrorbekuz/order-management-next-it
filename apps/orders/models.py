from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # new, processing, completed, cancelled
    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='new')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for Order {self.order.id}"
