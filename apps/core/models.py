from django.db import models

class MegaMenuBanner(models.Model):
    title = models.CharField(max_length=200, default="Premium Banana Chips")
    subtitle = models.CharField(max_length=200, default="Fresh • Crunchy • Healthy")
    image = models.ImageField(upload_to="mega_menu/")
    button_text = models.CharField(max_length=50, default="Shop Now")
    button_link = models.CharField(max_length=200, default="/products/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title