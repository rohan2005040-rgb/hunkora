from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("about/", views.about, name="about"),
    # path("reviews/", views.reviews, name="reviews"),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path("shop/", views.shop, name="shop"),
    # path("contact/", views.contact, name="contact")

]