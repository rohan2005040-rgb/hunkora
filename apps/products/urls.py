from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:id>/", views.product_detail, name="product_detail"),
    path(
    "wishlist/<int:id>/",
    views.toggle_wishlist,
    name="toggle_wishlist"),
    path(
    "shop/",
    views.shop,
    name="shop",),
    path(
        "search/",
        views.search_products,
        name="search_products",
    ),
]