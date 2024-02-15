from django.contrib import admin
from django.urls import path

from .views import profile_image, send_message_form, send_message

app_name = "app"
urlpatterns = [
    path('profile-image/<int:user_id>', profile_image),
    path('send-message-form/<int:user_id>', send_message_form, name="send-message-form"),
    path('send-message/', send_message)
]
