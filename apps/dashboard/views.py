from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.products.models import Product

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.contrib.auth import get_user_model
# অর্ডার ও ইউজার মডেল ইম্পোর্ট করার চেষ্টা (প্রজেক্টে থাকলে কাজ করবে)
try:
    from apps.orders.models import Order
except ImportError:
    Order = None

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    User = None

from django.contrib.auth.decorators import login_required
# ======================================================
# 1. Dashboard Overview (Main Dashboard Page)
# ======================================================
@login_required
def dashboard(request):
    # ১. প্রোডাক্ট এবং স্টক সামারি ডাটা
    total_products = Product.objects.count()
    
    # স্টক চেক ও লো স্টক কাউন্ট (যদি মডেল ফিল্ডে stock থাকে)
    try:
        low_stock_qs = Product.objects.filter(stock__lte=10)
        low_stock_count = low_stock_qs.count()
        low_stock_products = low_stock_qs.order_by('stock')[:5]
    except Exception:
        low_stock_products = Product.objects.all().order_by('-id')[:5]
        low_stock_count = 0

    recent_products = Product.objects.all().order_by('-id')[:5]

    # ২. অর্ডার এবং কাস্টমার সামারি ডাটা
    total_orders = Order.objects.count() if Order else 0
    recent_orders = Order.objects.all().order_by('-id')[:5] if Order else []
    total_customers = User.objects.filter(is_staff=False).count() if User else 0

    # মোট সেলস / রেভিনিউ গণনা (যদি total_amount ফিল্ড থাকে)
    try:
        total_sales = Order.objects.filter(
            Q(status__iexact='completed') | Q(status__iexact='delivered')
        ).aggregate(total=Sum('total_amount'))['total'] or 0
    except Exception:
        total_sales = 0

    # ৩. টপ সেলিং প্রোডাক্টস (Top Selling Products)
    try:
        # অথবা আপনার OrderItem মডেলের অ্যানোটেশন অনুযায়ী নিতে পারেন
        top_selling_products = Product.objects.annotate(
            total_sold=Sum('orderitem__quantity')
        ).order_by('-total_sold')[:5]
    except Exception:
        top_selling_products = Product.objects.all().order_by('-id')[:5]

    # ৪. সেলস চার্ট ডাটা (Sales Overview Chart - 7D, 30D, 12M)
    chart_7d_labels = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    chart_7d_data = [12000, 19000, 15000, 22000, 18000, 25000, 31000]

    chart_30d_labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    chart_30d_data = [85000, 112000, 98000, 145000]

    chart_12m_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    chart_12m_data = [210000, 240000, 190000, 280000, 320000, 310000, 390000, 420000, 380000, 450000, 490000, 520000]

    # ৫. টপবার নোটিফিকেশন ও মেসেজ কাউন্ট
    unread_notifications_count = 3  # ব্যাকএন্ড ডায়নামিক লজিক থাকলে তা বসিয়ে দিতে পারেন
    unread_messages_count = 5

    # ৬. কনটেক্সট ডিকশনারি
    context = {
        # কার্ড তথ্য
        "total_products": total_products,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "total_sales": total_sales,
        "low_stock_count": low_stock_count,  # <-- cards.html এরর ফিক্স
        "low_stock_products": low_stock_products,
        
        # লিস্ট ও টিবিল
        "recent_products": recent_products,
        "recent_orders": recent_orders,
        "top_selling_products": top_selling_products,

        # চার্ট ডাটা
        "chart_7d_labels": chart_7d_labels,
        "chart_7d_data": chart_7d_data,
        "chart_30d_labels": chart_30d_labels,
        "chart_30d_data": chart_30d_data,
        "chart_12m_labels": chart_12m_labels,
        "chart_12m_data": chart_12m_data,

        # টপবার
        "unread_notifications_count": unread_notifications_count,
        "unread_messages_count": unread_messages_count,
    }

    return render(request, "dashboard/dashboard.html", context)

# ======================================================
# 2. Product List
# ======================================================
def product_list(request):
    products = Product.objects.all().order_by("-id")
    context = {
        "products": products,
    }
    return render(
        request,
        "dashboard/products/product_list.html",
        context
    )


# ======================================================
# 3. Product Create
# ======================================================
def product_create(request):
    return render(request, "dashboard/products/product_create.html")


# ======================================================
# 4. Product Detail
# ======================================================
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product,
    }
    return render(request, "dashboard/products/product_detail.html", context)


# ======================================================
# 5. Product Update
# ======================================================
def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product,
    }
    return render(request, "dashboard/products/product_update.html", context)


# ======================================================
# 6. Product Delete
# ======================================================
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("dashboard:product_list")

    context = {
        "product": product,
    }
    return render(request, "dashboard/products/product_delete.html", context)



def search_view(request):
    query = request.GET.get('q', '')
    # আপনার সার্চ লজিক এখানে লিখুন
    context = {
        'query': query,
    }
    return render(request, 'dashboard/search_results.html', context)




@login_required
def profile_view(request):
    return render(request, 'dashboard/profile.html')


def order_list_view(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'dashboard/order_list.html', {'orders': orders})


def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'dashboard/order_detail.html', {'order': order})