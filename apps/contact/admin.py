
from django.contrib import admin
from .models import ContactMessage
# Register your models here.


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at') # অ্যাডমিন থেকে যেন কেউ মেসেজ এডিট করতে না পারে