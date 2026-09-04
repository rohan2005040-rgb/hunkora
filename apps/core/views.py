from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from apps.wishlist.models import Wishlist
from apps.products.models import Product
from apps.blogs.models import BlogPost
from apps.cart.models import Combo
from .models import MegaMenuBanner
from apps.products.models import Product
from products.models import Product
# ======================================
# HOME PAGE
# ======================================

def home(request):

    mega_banner = MegaMenuBanner.objects.filter(is_active=True).first()

    # ===========================
    # Best Selling Products
    # ===========================

    products = Product.objects.filter(
        is_active=True
    ).exclude(
        slug="spicy-masala-banana-chips"
    )[:2]

    wishlist_product_ids = []

    if request.user.is_authenticated:
        wishlist_product_ids = list(Wishlist.objects.filter(user=request.user).values_list("product_id", flat=True))

    # ===========================
    # Flavor Products
    # ===========================
    flavor_products = Product.objects.filter(
        is_active=True
    )[:3]

    # ===========================
    # Limited Offer Product
    # ===========================
    offer_product = Product.objects.filter(
        is_active=True
    ).first()

    # ===========================
    # New Arrival Products
    # ===========================
    new_products = Product.objects.filter(
        is_active=True
    ).order_by(
        "-created_at"
    )[:4]

    # ===========================
    # All Products
    # ===========================
    all_products = Product.objects.filter(
        is_active=True
    ).order_by(
        "-created_at"
    )

    # ===========================
    # Combo Offers
    # ===========================
    combos = Combo.objects.all().order_by("id")

    context = {

        "products": products,

        "offer_product": offer_product,

        "new_products": new_products,

        "all_products": all_products,

        "flavor_products": flavor_products,

        "combos": combos,
        "wishlist_product_ids": wishlist_product_ids,
        'mega_banner': mega_banner,


    }

    return render(
        request,
        "pages/home.html",
        context
    )


# ======================================
# ABOUT PAGE
# ======================================

def about(request):

    return render(
        request,
        "pages/about.html"
    )


# ======================================
# BLOG PAGE
# ======================================

def blogs(request):

    query = request.GET.get(
        "q",
        ""
    ).strip()

    if query:

        blogs = BlogPost.objects.filter(

            Q(title__icontains=query) |

            Q(content__icontains=query) |

            Q(category__icontains=query)

        ).distinct()

    else:

        blogs = BlogPost.objects.all().order_by(
            "-created_at"
        )

    context = {

        "blogs": blogs,

        "query": query,

    }

    return render(
        request,
        "pages/blogs.html",
        context
    )


# ======================================
# BLOG DETAIL
# ======================================

def blog_detail(request, id):

    blog = get_object_or_404(
        BlogPost,
        id=id
    )

    return render(
        request,
        "pages/blog_detail.html",
        {
            "blog": blog
        }
    )


# ======================================
# CONTACT PAGE
# ======================================

def contact(request):

    return render(
        request,
        "pages/contact.html"
    )


# ======================================
# SHOP PAGE
# ======================================
def shop(request):
    category = request.GET.get('category')
    
    # ক্যাটাগরি ফিল্টারিং
    if category and category != 'all':
        if category == 'original':
            products = Product.objects.filter(is_active=True, name__icontains='Original')
        elif category == 'magic-masala':
            products = Product.objects.filter(is_active=True, name__icontains='Magic Masala')
        elif category == 'spicy':
            products = Product.objects.filter(is_active=True, name__icontains='Spicy')
        else:
            products = Product.objects.filter(is_active=True)
    else:
        products = Product.objects.filter(is_active=True)

    context = {
        'products': products
    }
    return render(request, "shop/shop.html", context)