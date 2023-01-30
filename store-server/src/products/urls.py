from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name='index'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
