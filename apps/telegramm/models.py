# models.py
from django.db import models


class TelegramUser(models.Model):
    username = models.CharField(max_length=255)
    id_user = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
   
    chat_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Make sure this line exists

    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = 'польватель телеграмма'
        verbose_name_plural = 'пользователи телеграмма'