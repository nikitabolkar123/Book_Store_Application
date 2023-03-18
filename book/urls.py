from django.urls import path

from . import views

urlpatterns = [
    path('book_store/', views.BookAPIViews.as_view(), name='book_store'),
    path('book_store/<int:book_id>/', views.BookAPIViews.as_view(), name='book_store'),

]
#
