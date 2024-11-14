from django.contrib import admin
from .models import TelegramUser
# Register your models here.
@admin.register(TelegramUser)
class TelegramUserSettings(admin.ModelAdmin):
    list_display = ['id','username','first_name']