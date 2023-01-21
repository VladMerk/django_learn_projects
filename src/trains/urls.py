from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrainsListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.TrainsDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.TrainsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TrainsDeleteView.as_view(), name='delete'),
    path('add/', views.TrainsCreateView.as_view(), name='create'),
]
