from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [

    path("", views.dashboard, name="dashboard"),
    path("products/",views.product_list,name="product_list"),

    path("products/add/", views.product_create, name="product_create"),

    path("products/<int:id>/", views.product_detail, name="product_detail"),

    path("products/<int:id>/edit/", views.product_update, name="product_update"),

    path("products/<int:id>/delete/", views.product_delete, name="product_delete"),
    path('search/', views.search_view, name='search'),
    path('profile/', views.profile_view, name='profile'),
    path('orders/', views.order_list_view, name='order_list'),
    path('orders/<int:pk>/', views.order_detail_view, name='order_detail'),

]