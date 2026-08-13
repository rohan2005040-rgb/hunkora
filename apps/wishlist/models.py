from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist_items",
        null=True,
        blank=True,
    )

    session_key = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlist_products",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.product.name