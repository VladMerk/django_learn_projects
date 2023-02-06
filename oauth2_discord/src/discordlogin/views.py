import requests
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from requests import Session
from django.conf import settings

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1023904638992396330&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect%2F&response_type=code&scope=identify"


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return JsonResponse({
            "msg": "Hello World!",
            "user_id": request.user.id,
            "user_discord_tag": request.user.discord_tag,
            "user_last_login": request.user.last_login,
        })
    return JsonResponse({'msg': 'Is not authenticated'})

def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)

def get_authenticated_user(request: HttpRequest):
  print(request.user)
  user = request.user
  return JsonResponse({
    "id": user.id,
    "discord_tag": user.discord_tag,
    "last_login": user.last_login,
    "avatar": user.avatar,
    "locale": user.locale,
    'mfa': user.mfa_enabled,
    "public_flags": user.public_flags
  })



def discord_login_redirect(request: HttpRequest):
    code = request.GET.get("code")
    user = exchange_code(code)
    discord_user = authenticate(request=request, user=user)
    discord_user = list(discord_user).pop()
    login(request=request, user=discord_user)
    return redirect(reverse('auth_user'))


def exchange_code(code: str):
    data = {
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect/",
        "scope": "identify",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = Session().post(
        url="https://discord.com/api/oauth2/token", data=data, headers=headers
    )
    credentials = response.json()
    access_token = credentials["access_token"]
    response = requests.get(
        "https://discord.com/api/v10/users/@me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return response.json()
