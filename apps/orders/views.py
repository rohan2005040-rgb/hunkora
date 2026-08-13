from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Order, OrderItem
from apps.cart.models import Cart, CartItem
from apps.accounts.models import UserProfile


@login_required(login_url="accounts:register")
def checkout_view(request):
    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart = Cart.objects.filter(session_key=session_key).first()

    if not cart:
        return redirect("cart:cart")

    cart_items = CartItem.objects.filter(cart=cart)

    subtotal = sum(item.total_price() for item in cart_items)
    shipping = 65
    vat = 0
    grand_total = subtotal + shipping

    # ইউজারের সেভ থাকা প্রোফাইল ডেটা অথবা নতুন প্রোফাইল গেট/ক্রিয়েট করা
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")
        landmark = request.POST.get("landmark")
        payment_method = request.POST.get("payment_method")

        # ১. অর্ডার তৈরি করা
        order = Order.objects.create(
            user=request.user,
            order_id="HKR" + timezone.now().strftime("%Y%m%d%H%M%S"),
            full_name=full_name,
            phone=phone,
            city=city,
            address=address,
            landmark=landmark,
            payment_method=payment_method,
            subtotal=subtotal,
            shipping_charge=shipping,
            grand_total=grand_total,
            bkash_number=request.POST.get("bkash_number"),
            transaction_id=request.POST.get("transaction_id"),
            payment_status="Pending",
        )

        # ২. ইউজারের বিলিং এড্রেস ও ফোন নম্বর প্রোফাইলে সেভ/আপডেট করে দেওয়া
        full_address_text = f"{address}, {city}" if city else address
        if landmark:
            full_address_text += f" (Landmark: {landmark})"
            
        profile.address = full_address_text
        if phone:
            profile.phone_number = phone
        profile.save()

        # ফার্স্ট নেম/লাস্ট নেম খালি থাকলে আপডেট করে দেওয়া
        if full_name and not request.user.first_name:
            names = full_name.strip().split(' ', 1)
            request.user.first_name = names[0]
            if len(names) > 1:
                request.user.last_name = names[1]
            request.user.save()

        # ৩. কার্টের আইটেমগুলো অর্ডার আইটেমে ট্রান্সফার করা
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # ৪. কার্ট ক্লিয়ার করা
        cart_items.delete()
        cart.delete()

        return redirect("orders:order_success")

    # GET রিকোয়েস্টে ফর্ম ফিল্ডের জন্য সেভ থাকা তথ্য পাঠানো
    saved_initial_data = {
        "full_name": f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
        "phone": profile.phone_number or "",
        "address": profile.address or "",
    }

    context = {
        "cart": cart,
        "cart_items": cart_items,
        "cart_total": subtotal,
        "grand_total": grand_total,
        "saved_data": saved_initial_data,
    }

    return render(
        request,
        "pages/checkout.html",
        context
    )


def order_success(request):
    return render(request, "pages/order_success.html")