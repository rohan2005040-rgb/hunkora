
from django.shortcuts import render
from django.db.models import Q
from .models import BlogPost

# Create your views here.
# def blog_list(request):
#     query = request.GET.get('q', '').strip()
    
#     # ডাটাবেজে ব্লগ আছে কি না চেক করবে
#     if query:
#         blogs = BlogPost.objects.filter(
#             Q(title__icontains=query) | 
#             Q(content__icontains=query) |
#             Q(category__icontains=query)
#         ).order_by('-created_at')
#     else:
#         blogs = BlogPost.objects.all().order_by('-created_at')

#     context = {
#         'blogs': blogs,
#         'query': query,
#     }
    
#     # আপনার টেমপ্লেটের সঠিক ফাইলের নাম দিন (blog_list.html অথবা blogs.html)
#     return render(request, 'blog_list.html', context)