from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order,OrderItem


class OrderAdmin(admin.ModelAdmin):

    list_display=(

        "order_id",

        "full_name",

        "phone",

        "payment_method",

        "payment_status",

        "status",

        "created_at",

    )

admin.site.register(
    Order,
    OrderAdmin
)

admin.site.register(OrderItem)