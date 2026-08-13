from django.contrib import admin
from .models import Review
# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "rating",
        "is_approved",
        "created_at",
    )

    list_filter = (
        "rating",
        "is_approved",
    )

    search_fields = (
        "name",
        "email",
    )