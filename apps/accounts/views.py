from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

# Wishlist অ্যাপ ইমপোর্ট (যদি থাকে)
try:
    from apps.products.models import Wishlist
except ImportError:
    Wishlist = None

# Order অ্যাপ ইমপোর্ট
try:
    from apps.orders.models import Order
except ImportError:
    Order = None


@login_required(login_url='accounts:login')
def profile_view(request):
    user = request.user
    # ইউজারের প্রোফাইল না থাকলে স্বয়ংক্রিয়ভাবে তৈরি করে নেবে
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        # ১. ক্যামেরা আইকন বা Quick Avatar Upload ফর্ম থেকে পিকচার আসলে
        if 'avatar' in request.FILES and len(request.POST) <= 2:  # শুধু অ্যাভাটার ফর্ম সাবমিট হলে
            profile.avatar = request.FILES['avatar']
            profile.save()
            messages.success(request, 'Profile picture updated successfully!')
            return redirect('accounts:profile')

        # ২. এডিট প্রোফাইল (Main Edit Profile Form) এর ডাটা সেভ করা
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        address = request.POST.get('address', '').strip()

        # User মডেলের বেসিক ডাটা আপডেট
        user.first_name = first_name
        user.last_name = last_name
        if email:
            user.email = email
        user.save()

        # UserProfile মডেলের ডাটা (Phone, Address, Avatar) আপডেট
        profile.phone_number = phone_number
        profile.address = address

        # মূল এডিট ফর্মে যদি ছবি সিলেক্ট করা হয়ে থাকে
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        profile.save()

        messages.success(request, 'Your profile details updated successfully!')
        return redirect('accounts:profile')

    # ইউজারের আগের অর্ডারের লিস্ট ফিল্টার করা
    orders = []
    if Order is not None:
        try:
            orders = Order.objects.filter(user=user).order_by('-created_at')
        except Exception:
            orders = []

    # ইউজারের উইশলিস্ট ফিল্টার করা
    wishlist_items = []
    if Wishlist is not None:
        try:
            wishlist_items = Wishlist.objects.filter(user=user)
        except Exception:
            wishlist_items = []

    context = {
        'user': user,
        'profile': profile,
        'orders': orders,
        'orders_count': len(orders),
        'wishlist_items': wishlist_items,
        'wishlist_count': len(wishlist_items),
        'reward_points': getattr(profile, 'reward_points', 150),
    }
    
    return render(request, 'accounts/profile.html', context)


def login_view(request):
    # ইউজার আগে থেকেই লগইন থাকলে প্রোফাইলে পাঠিয়ে দেওয়া
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # যদি ইউজারনেমের বদলে ইমেইল দিয়ে লগইন করতে চায়
        if '@' in username_or_email:
            user_obj = User.objects.filter(email=username_or_email).first()
            if user_obj:
                username_or_email = user_obj.username

        # ইউজারের ক্রিডেনশিয়াল ভেরিফাই করা
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            # লগইন করার পর আগের কোনো পেজ (যেমন Checkout) থেকে এসে থাকলে সেখানে রিডাইরেক্ট করা
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Invalid username/email or password!')

    return render(request, 'accounts/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # ১. ইউজারনেম খালি কিনা চেক
        if not username:
            messages.error(request, 'Please provide a valid username!')
            return render(request, 'accounts/register.html')

        # ২. পাসওয়ার্ড মিলছে কিনা চেক
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'accounts/register.html')

        # ৩. ইউজারনেম আগে থেকে আছে কিনা চেক
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken!')
            return render(request, 'accounts/register.html')

        # ৪. ইমেইল আগে থেকেই আছে কিনা চেক
        if email and User.objects.filter(email=email).exists():
            messages.error(request, 'Email address is already registered!')
            return render(request, 'accounts/register.html')

        # ফার্স্ট ও লাস্ট নেম আলাদা করা
        names = full_name.split(' ', 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ''

        # ৫. ইউজার তৈরি করা
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # ৬. প্রোফাইল ও ফোন নম্বর সেভ করা
        profile, created = UserProfile.objects.get_or_create(user=user)
        if phone_number:
            profile.phone_number = phone_number
            profile.save()

        # ৭. অটো লগইন করিয়ে প্রোফাইলে পাঠানো
        login(request, user)
        messages.success(request, f'Account created successfully! Welcome, {user.first_name or user.username}.')
        return redirect('accounts:profile')

    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('accounts:login')