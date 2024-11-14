from django.shortcuts import render, redirect
from apps.settings.models import Blog, Contact
from apps.telegramm.views import get_text


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', locals())

def friends(request):
    blogs = Blog.objects.all()
    return render(request,'friends.html',locals())





def send_message(request):
    
    get_text('Ты — всё, о чём я мечтал. Люблю тебя и хочу, чтобы мы были вместе')
    return redirect('index')



































