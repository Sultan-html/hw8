from django.shortcuts import render, redirect
from apps.settings.models import Blog, Contact
# Create your views here.
from apps.telegram.views import get_text

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', locals())

def friends(request):
    blogs = Blog.objects.all()
    return render(request,'friends.html',locals())

def contact(request):
    contact= Contact.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name,  email=email, message=message)
    
    
        get_text(f""" Оставлен отзыв 
                      Имя пользователя: {name}
                      Адрес(email): {email}
                      Сообщение: {message}
""")
        return redirect('main')

    return render(request, "index.html", locals())