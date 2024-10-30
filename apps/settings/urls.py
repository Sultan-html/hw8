from django.urls import path
from apps.settings.views import index,friends

urlpatterns = [
    path('',index,name='index'),
    path('friends/',friends,name='friends')
]
