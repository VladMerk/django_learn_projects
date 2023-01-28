from django.urls import path

from object import views

urlpatterns = [
    path('', views.ObjectListView.as_view(), name='index'),
    path('create/', views.ObjectCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.ObjectDeleteView.as_view(), name='delete'),
    path('api/teams/<int:city_id>', views.get_team, name='get_teams'),
    path('api/object/<int:team_id>', views.get_object, name='get_object'),
]
