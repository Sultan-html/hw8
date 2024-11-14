from django.urls import path
from apps.settings.views import index,friends,send_message

urlpatterns = [
    path('',index,name='index'),
    path('photo/',friends,name='photo'),
    path('send_message/', send_message, name='send_message'),

]
