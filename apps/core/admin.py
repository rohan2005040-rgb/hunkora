from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MegaMenuBanner

@admin.register(MegaMenuBanner)
class MegaMenuBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')