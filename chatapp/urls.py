from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.chatroom, name='chatroom'),
]
