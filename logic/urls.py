from .views import Home,chat
import AI
from django.urls import path
urlpatterns = [
    path('',Home),
    path('chat',chat),
]