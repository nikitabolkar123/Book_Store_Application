from django.urls import path

from . import views

urlpatterns = [
    path('cart_item/', views.CartItemViews.as_view(), name='cart_item'),
]
