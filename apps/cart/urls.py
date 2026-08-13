from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [

    # =========================
    # Cart Page
    # =========================

    path(
        "",
        views.cart_view,
        name="cart"
    ),

    # =========================
    # Add To Cart
    # =========================

    path(
        "add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    # =========================
    # Increase Quantity
    # =========================

    path(
        "increase/<int:item_id>/",
        views.increase_quantity,
        name="increase_quantity"
    ),

    # =========================
    # Decrease Quantity
    # =========================

    path(
        "decrease/<int:item_id>/",
        views.decrease_quantity,
        name="decrease_quantity"
    ),

    # =========================
    # Remove Product
    # =========================

    path(
        "remove/<int:item_id>/",
        views.remove_item,
        name="remove_item"
    ),
    # =========================
    # ADD COMBO
    # =========================

    path(
        "add-combo/<int:combo_id>/",
        views.add_combo,
        name="add_combo"
    ),

]
