from django.urls import path
from . import views

app_name = 'seller_panel'

urlpatterns = [
    path('', views.seller_dashboard, name='dashboard'),
    path('order/<int:pk>/manage/', views.update_order_status, name='manage_order'),
]