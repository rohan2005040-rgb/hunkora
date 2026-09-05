from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from apps.orders.models import Order

@login_required(login_url='account:login')
def seller_dashboard(request):
    # ইউজার স্টাফ কি না চেক করা
    if not request.user.is_staff:
        messages.error(request, "আপনার সেলার ড্যাশবোর্ডে প্রবেশের অনুমতি নেই।")
        return redirect('account:profile')

    # ওভারভিউ ও অ্যানালিটিক্স
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending')
    delivered_orders = Order.objects.filter(status='Delivered')

    # মোট সেলের হিসাব
    total_sales = Order.objects.filter(status='Delivered').aggregate(Sum('grand_total'))['grand_total__sum'] or 0

    context = {
        'total_orders': total_orders,
        'pending_count': pending_orders.count(),
        'delivered_count': delivered_orders.count(),
        'total_sales': total_sales,
        'recent_orders': Order.objects.all().order_by('-created_at')[:15],
    }
    return render(request, 'seller_panel/dashboard.html', context)

@login_required(login_url='account:login')
def update_order_status(request, pk):
    if not request.user.is_staff:
        messages.error(request, "আপনার এই অ্যাকশনটি সম্পন্ন করার অনুমতি নেই।")
        return redirect('account:profile')

    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.courier_name = request.POST.get('courier_name')
        order.tracking_id = request.POST.get('tracking_id')
        order.save()
        return redirect('seller_panel:dashboard')

    return render(request, 'seller_panel/order_manage.html', {'order': order})