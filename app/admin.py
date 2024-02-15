from django.utils.html import format_html
from django.contrib import admin
from django.urls import reverse
from django.urls import path, re_path
from .models import Users
from django.http import HttpResponse
# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["view_image", "first_name", "last_name", "view_telegram_id", "view_username", "view_phone", "view_send_button"]
    list_display_links = ["view_image", "first_name", "last_name"]

    fields = ["view_telegram_id", "view_image", "first_name", "last_name", "phone", "view_username"]
    readonly_fields = ["view_telegram_id", "view_image", "view_username"]

    change_list_template = "my_changelist.html"

    @admin.display(description="")
    def view_send_button(self, obj: Users):
        # url = reverse('app:send-message', args=[obj.pk]),
        return format_html(
            f"""
            <div class="related-widget-wrapper" data-model-ref="sendMess">
                <a class="related-widget-wrapper-link btn btn-primary" data-popup="yes" href="/send-message-form/{obj.id}" style="font-size: 0.6rem">Отправить сообщение</a>
            </div>
            """,
        )

    @admin.display(description="Телефон")
    def view_phone(self, obj: Users):
        return format_html(f'<a href="tel:{obj.phone}">{obj.phone}</a>')
    
    @admin.display(description="Ник")
    def view_username(self, obj: Users):
        return format_html(f'<a href="tg://{obj.username}">@{obj.username}</a>')

    @admin.display(description="Телеграм ID")
    def view_telegram_id(self, obj: Users):
        return format_html(f'<a href="tg://user?id={obj.telegram_id}">{obj.telegram_id}</a>')
    
    @admin.display(description='Изображение')
    def view_image(self, obj: Users) -> str:
        if obj.image_telegram_path:
            return format_html(f'<img style="border-radius: 50%" src="/profile-image/{obj.telegram_id}" height="25"/>')

        else:
            return format_html('<img style="border-radius: 50%" src="https://www.svgrepo.com/show/376230/status-notfound.svg" height="25"/>')

    # @admin.action(description="Mark selected stories as published")
    # def send_all_message(modeladmin, request, queryset):
        
    #     return format_html(f'<script type="text/javascript">/send-message-form/4</script>')

    # actions = [send_all_message]