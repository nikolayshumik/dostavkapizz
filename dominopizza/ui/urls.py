from django.urls import path
from .import views

urlpatterns = [
    path('pizza/', views.pizza, name='pizza'),
    path('order/<int:pizza_id>/', views.order, name='order'),
    path('order/complete/', views.order_complete, name='order_complete'),
]