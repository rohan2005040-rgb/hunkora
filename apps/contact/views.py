from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # ডাটাবেজে সেভ করা
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, 'Thank you! Your message has been sent successfully.')
        return redirect('contact')  # আপনার কন্টাক্ট পেজের URL নাম দিন

    return render(request, 'pages/contact.html')
