"""oauth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from discordlogin import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/user", views.get_authenticated_user, name="auth_user"),
    path("oauth2/", views.home, name="oauth2"),
    path("oauth2/login/", views.discord_login, name="oauth_discord"),
    path(
        "oauth2/login/redirect/",
        views.discord_login_redirect,
        name="discord_login_redirect",
    ),
]
