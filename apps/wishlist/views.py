from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# ✅ শুধু সঠিক Model ইমপোর্ট রাখা হয়েছে
from apps.products.models import Wishlist, Product


# ==========================================
# Wishlist Page
# ==========================================
@login_required(login_url="accounts:login")
def wishlist(request):

    items = Wishlist.objects.filter(
        user=request.user
    ).select_related("product")

    context = {
        "items": items,
    }

    return render(
        request,
        "wishlist/wishlist.html",
        context,
    )


# ==========================================
# Add To Wishlist
# ==========================================
@login_required(login_url="accounts:login")
def add_to_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product,
    )

    return redirect(request.META.get("HTTP_REFERER", "/"))


# ==========================================
# Remove From Wishlist
# ==========================================
@login_required(login_url="accounts:login")
def remove_from_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    Wishlist.objects.filter(
        user=request.user,
        product=product,
    ).delete()

    return redirect(request.META.get("HTTP_REFERER", "/"))