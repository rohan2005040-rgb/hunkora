from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from apps.orders.models import Order

def seller_dashboard(request):
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status__iexact='Pending').count()
    confirmed_orders = Order.objects.filter(status__iexact='Confirmed').count()
    delivered_orders = Order.objects.filter(status__iexact='Delivered').count()

    total_sales = Order.objects.filter(status__iexact='Delivered').aggregate(Sum('grand_total'))['grand_total__sum'] or 0

    orders = Order.objects.all().order_by('-created_at')

    context = {
        'total_orders': total_orders,
        'pending_count': pending_orders,
        'confirmed_count': confirmed_orders,
        'delivered_count': delivered_orders,
        'total_sales': total_sales,
        'recent_orders': orders,
    }
    return render(request, 'seller_panel/dashboard.html', context)

def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
        return redirect('seller_panel:dashboard')
    return render(request, 'seller_panel/order_manage.html', {'order': order})