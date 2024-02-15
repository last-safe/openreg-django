from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Users(models.Model):
    telegram_id = models.IntegerField(verbose_name="Телеграм ID", editable=False)
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", max_length=64, blank=True)
    username = models.CharField(verbose_name="Ник", max_length=35, blank=True)
    language_code = models.CharField(verbose_name="Язык", max_length=2, blank=True, null=True, editable=False)
    is_premium = models.BooleanField(verbose_name="Премиум", blank=True, null=True, editable=False)

    phone = PhoneNumberField(verbose_name="Телефон", blank=True)
    image_telegram_path = models.CharField(max_length=100, blank=True, editable=False)


    def __str__(self) -> str:
        return str(self.telegram_id)
    
    class Meta:
        verbose_name = "пользователь телеграмм"
        verbose_name_plural = "Пользователи тг"