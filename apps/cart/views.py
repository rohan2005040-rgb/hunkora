from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.products.models import Product
from .models import Cart, CartItem, Combo
from .models import Cart, CartItem
from apps.products.models import Product



# ==========================================
# ADD SINGLE PRODUCT
# ==========================================

@login_required(login_url="accounts:register")
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    weight = int(request.GET.get("weight", 100))

    if weight == 50:
        price = product.price / 2
    elif weight == 100:
        price = product.price
    elif weight == 200:
        price = product.price * 2
    else:
        price = product.price

    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(
        session_key=session_key
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        combo=None,
        weight=weight,
        defaults={
            "price": price,
            "quantity": 1,
        }
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart:cart")


# ==========================================
# ADD COMBO
# ==========================================

@login_required(login_url="accounts:register")
def add_combo(request, combo_id):

    combo = get_object_or_404(
        Combo,
        id=combo_id
    )

    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(
        session_key=session_key
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        combo=combo,
        product=None,
        defaults={
            "price": combo.price,
            "weight": combo.weight,
            "quantity": 1,
        }
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart:cart")


# ==========================================
# CART PAGE
# ==========================================

def cart_view(request):

    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart = Cart.objects.filter(
        session_key=session_key
    ).first()

    cart_total = 0

    if cart:
        for item in cart.items.all():
            cart_total += item.total_price()

    context = {
        "cart": cart,
        "cart_total": cart_total,
    }

    return render(
        request,
        "pages/cart.html",
        context
    )


# ==========================================
# INCREASE QUANTITY
# ==========================================

def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id
    )

    item.quantity += 1
    item.save()

    return redirect("cart:cart")


# ==========================================
# DECREASE QUANTITY
# ==========================================

def decrease_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart:cart")


# ==========================================
# REMOVE ITEM
# ==========================================

def remove_item(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id
    )

    item.delete()

    return redirect("cart:cart")