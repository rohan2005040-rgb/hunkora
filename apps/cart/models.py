from django.db import models
from apps.products.models import Product


class Cart(models.Model):
    session_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_key


# ==========================================
# COMBO MODEL
# ==========================================
class Combo(models.Model):

    BADGE_CHOICES = [
        ("NORMAL", "NORMAL"),
        ("BEST VALUE", "BEST VALUE"),
        ("FAMILY", "FAMILY"),
        ("LIMITED", "LIMITED"),
    ]

    name = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="combos/"
    )

    description = models.TextField(
        blank=True
    )

    badge = models.CharField(
        max_length=30,
        choices=BADGE_CHOICES,
        default="NORMAL"
    )

    packets = models.PositiveIntegerField()

    weight = models.PositiveIntegerField(
        help_text="Example : 300"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    button_text = models.CharField(
        max_length=100,
        default="Shop Now"
    )

    # NEW FEATURE FIELD

    features = models.TextField(
        help_text="""
Write one feature per line.

Example

3 Premium Banana Chips
Freshly Prepared
Free Delivery
Best Value
"""
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = ["id"]

    @property
    def save_amount(self):
        if hasattr(self, 'old_price') and self.old_price is not None and self.price is not None:
            try:
                return float(self.old_price) - float(self.price)
            except (ValueError, TypeError):
                return 0
        return 0
            

        # return self.old_price - self.price

    @property
    def feature_list(self):

        if not self.features:
            return []

        return [
            x.strip()
            for x in self.features.splitlines()
            if x.strip()
        ]

    def __str__(self):

        return self.name
# ==========================================
# CART ITEM
# ==========================================

class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    combo = models.ForeignKey(
        Combo,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    weight = models.PositiveIntegerField(
        default=100
    )

    def total_price(self):
        return self.price * self.quantity

    @property
    def total_weight(self):
        return self.weight * self.quantity