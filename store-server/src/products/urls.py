from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # path('', cache_page(30)(views.ProductListView.as_view()), name='index'),
    path('', views.ProductListView.as_view(), name='index'),
    path('category/<int:category_id>/', views.ProductListView.as_view(), name='category'),
    path('page/<int:page>/', views.ProductListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
