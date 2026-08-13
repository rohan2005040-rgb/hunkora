from apps.products.models import Wishlist


def wishlist(request):

    count = 0

    if request.user.is_authenticated:

        count = Wishlist.objects.filter(
            user=request.user
        ).count()

    return {

        "wishlist_count": count,

    }