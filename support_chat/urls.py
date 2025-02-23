from django.urls import path
from support_chat import views

urlpatterns = [
    path("", views.chat_page, name="chat_page"),
]
