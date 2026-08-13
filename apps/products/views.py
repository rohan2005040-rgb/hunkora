from django.shortcuts import render, get_object_or_404
from apps.products.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Product, Wishlist
def shop(request):
    query = request.GET.get("q")

    products = Product.objects.filter(is_active=True)

    if query:
        products = products.filter(name__icontains=query)

    return render(
        request,
        "products/shop.html",
        {
            "products": products,
            "query": query,
        }
    )
# =========================================================
# product_list
# =======================================================
from .models import Product, Wishlist

def product_list(request):

    products = Product.objects.filter(is_active=True)

    wishlist_product_ids = []

    if request.user.is_authenticated:

        wishlist_product_ids = list(
    Wishlist.objects.filter(
        user=request.user
    ).values_list(
        "product_id",
        flat=True
    ))

    context = {

    "products": products,

    "wishlist_product_ids": wishlist_product_ids,}

    return render(

        request,

        "pages/products.html",

        context

    )
# ==============================================================
# product_detail
# =========================================

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "pages/product-details.html", {"product": product})

@login_required
def toggle_wishlist(request, id):

    product = Product.objects.get(id=id)

    wishlist = Wishlist.objects.filter(
        user=request.user,
        product=product
    )

    if wishlist.exists():
        wishlist.delete()
    else:
        Wishlist.objects.create(
            user=request.user,
            product=product
        )

    return redirect(request.META.get("HTTP_REFERER", "/"))


def search_products(request):
    query = request.GET.get("q")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    return render(request, "pages/products.html", {
        "products": products,
        "query": query,
    })