from django.urls import path

from teams import views

urlpatterns = [
    path("", views.TeamsListView.as_view(), name='index'),
    path("create/", views.TeamCreateView.as_view(), name='create'),
    path("update/<int:pk>/", views.TeamUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", views.TeamDeleteView.as_view(), name='delete'),
]
