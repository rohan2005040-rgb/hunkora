from django.contrib import admin
from .models import Product, Wishlist


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "stock",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        ("Product Information", {
            "fields": (
                "name",
                "slug",
                "short_description",
                "description",
            )
        }),

        ("Images", {
            "fields": (
                "image",
                "custom_image",
                "image2",
                "image3",
                "image4",
                "video",
            )
        }),

        ("Pricing", {
            "fields": (
                "price",
                "old_price",
            )
        }),

        ("Inventory", {
            "fields": (
                "stock",
                "is_active",
            )
        }),

        ("Dates", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),

    )


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "created_at",
    )

    search_fields = (
        "user__username",
        "product__name",
    )

    list_filter = (
        "created_at",
    )