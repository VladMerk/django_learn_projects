from django.urls import path

from . import views

urlpatterns = [
    path('', views.CitiesListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.CitiesDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CitiesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CitiesDeleteView.as_view(), name='delete'),
    path('add/', views.CitiesCreateView.as_view(), name='create'),
]
