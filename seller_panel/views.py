from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from apps.orders.models import Order

def seller_dashboard(request):
    # মোট অর্ডার, পেন্ডিং অর্ডার ও ডেলিভার্ড অর্ডার
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending')
    delivered_orders = Order.objects.filter(status='Delivered')

    # মোট সেলস
    total_sales = Order.objects.filter(status='Delivered').aggregate(Sum('grand_total'))['grand_total__sum'] or 0

    context = {
        'total_orders': total_orders,
        'pending_count': pending_orders.count(),
        'delivered_count': delivered_orders.count(),
        'total_sales': total_sales,
        'recent_orders': Order.objects.all().order_by('-created_at')[:15],
    }
    # সরাসরি সেলার ড্যাশবোর্ড HTML লোড হবে
    return render(request, 'seller_panel/dashboard.html', context)

def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.courier_name = request.POST.get('courier_name')
        order.tracking_id = request.POST.get('tracking_id')
        order.save()
        return redirect('seller_panel:dashboard')

    return render(request, 'seller_panel/order_manage.html', {'order': order})