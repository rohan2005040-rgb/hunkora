from django.db import models
from django.conf import settings
# Create your models here.
class Order(models.Model):

    ORDER_STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    PAYMENT_METHOD = [
        ("COD", "Cash On Delivery"),
        ("BKASH", "bKash"),
        ("NAGAD", "Nagad"),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='orders'
    )

    order_id = models.CharField(max_length=30, unique=True)

    full_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=100)

    address = models.TextField()

    landmark = models.CharField(max_length=255, blank=True)

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)

    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)

    bkash_number = models.CharField(max_length=20,blank=True,null=True)

    transaction_id = models.CharField(max_length=100,blank=True,null=True)

    payment_status = models.CharField(max_length=20,default="Pending")

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def total(self):
        return self.quantity * self.price