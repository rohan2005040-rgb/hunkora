from django.db import models
from django.conf import settings
class Product(models.Model):

    CATEGORY_CHOICES = [
        ("original", "Original"),
        ("magic-masala", "Magic Masala"),
        ("spicy", "Spicy"),
        ("combo", "Combo"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="original",
    )

    is_best_seller = models.BooleanField(default=False)

    image = models.ImageField(upload_to="products/")

    custom_image = models.ImageField(
        upload_to="custom_products/",
        blank=True,
        null=True,
    )

    image2 = models.ImageField(upload_to="products/", blank=True, null=True)
    image3 = models.ImageField(upload_to="products/", blank=True, null=True)
    image4 = models.ImageField(upload_to="products/", blank=True, null=True)

    video = models.FileField(
        upload_to="products/videos/",
        blank=True,
        null=True,
    )

    short_description = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# =========================================================
# Wishlist
# ========================================================
class Wishlist(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} - {self.product}"