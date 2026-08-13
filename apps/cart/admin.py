from django.contrib import admin
from django.utils.html import format_html

from .models import Cart, CartItem, Combo


# ==========================================================
# CART ITEM INLINE
# ==========================================================

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


# ==========================================================
# CART
# ==========================================================

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "session_key",
        "created_at",
    )

    search_fields = (
        "session_key",
    )

    readonly_fields = (
        "created_at",
    )

    inlines = [
        CartItemInline,
    ]


# ==========================================================
# CART ITEM
# ==========================================================

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "combo",
        "quantity",
        "weight",
        "price",
        "total_price",
    )

    list_filter = (
        "product",
        "combo",
    )

    search_fields = (
        "product__name",
        "combo__name",
    )


# ==========================================================
# COMBO
# ==========================================================

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "name",
        "badge",
        "packets",
        "weight",
        "price",
        "old_price",
        "save_amount",
        "is_active",
    )

    list_editable = (
        "price",
        "old_price",
        "is_active",
    )

    list_filter = (
        "badge",
        "is_active",
    )

    search_fields = (
        "name",
        "features",
    )

    readonly_fields = (
        "image_preview",
        "save_amount",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "image",
                    "image_preview",
                    "description",
                    "badge",
                )
            },
        ),

        (
            "Price Information",
            {
                "fields": (
                    "price",
                    "old_price",
                    "save_amount",
                )
            },
        ),

        (
            "Packet Information",
            {
                "fields": (
                    "packets",
                    "weight",
                )
            },
        ),

        (
            "Combo Features",
            {
                "fields": (
                    "features",
                ),
                "description": "Write one feature per line.",
            },
        ),

        (
            "Button",
            {
                "fields": (
                    "button_text",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),

    )

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;">',
                obj.image.url,
            )

        return "-"

    image_preview.short_description = "Preview"