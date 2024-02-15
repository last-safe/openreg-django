from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Users

import urllib.request
from urllib.parse import urlparse, urlencode

from bot.main import bot
import asyncio

# Create your views here.
def profile_image(request, user_id: int):
    target_user = Users.objects.get(telegram_id = user_id)
    print(f"https://api.telegram.org/file/bot{settings.TELEGRAM_TOKEN}/{target_user.image_telegram_path}")
    with urllib.request.urlopen(f"https://api.telegram.org/file/bot{settings.TELEGRAM_TOKEN}/{target_user.image_telegram_path}") as file:
        return HttpResponse(file.read(), content_type="image/png")

def send_message_form(request, user_id: int):
    return render(request, "send_form.html", {"user_id": user_id})


def send_message(request):
    if request.method == 'GET' and request.GET.get("message"):
        if int(request.GET["user_id"]):
            target_users = Users.objects.filter(id = request.GET["user_id"])
        else:
            target_users = Users.objects.all()


        url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
        for user in target_users:
            params = {
                "chat_id" : user.telegram_id,
                "text" : request.GET["message"],
                "parse_mode" : "html",
            }
            
            url += ('&', '?')[urlparse(url).query == ''] + urlencode(params)

            urllib.request.urlopen(url)
        
        return HttpResponse('<script type="text/javascript">window.close()</script>')
    