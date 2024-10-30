from django.shortcuts import render, redirect
from apps.settings.models import Blog, Contact
from apps.telegram.models import TelegramUser
from telebot import TeleBot, types
TELEGRAM_TOKEN = "8021147059:AAGmYzPKSGv9ECsZuNRKUeUhj2LyRRd93QU"
ADMIN_ID =  5420298695

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admin_id = ADMIN_ID

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_message(message:types.Message):
    mail.description = message.text 
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.id_user, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != int(admin_id):
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message)

def get_text_doctor(message, id):
    bot.send_message(id, message)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}")

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})  # Передаем контекст в виде словаря

def friends(request):
    blogs = Blog.objects.all()
    return render(request, 'friends.html', {'blogs': blogs})  # Передаем контекст в виде словаря
