from django.core.management.base import BaseCommand
from apps.telegramm.views import bot

class Command(BaseCommand):
    help = 'Bot' 

    def handle(self, *args, **kwargs):
        print("START TELEGRAM BOT")
        bot.polling(none_stop=True, interval=0)