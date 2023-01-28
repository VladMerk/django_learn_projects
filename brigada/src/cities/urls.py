from django.urls import path

from cities import views

urlpatterns = [
    path('', views.CityListView.as_view(), name='index'),
    path('create/', views.CityCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='delete'),
]
