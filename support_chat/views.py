

from django.shortcuts import render
from django.http import HttpResponse

def chat_page(request):
    return HttpResponse("Hello, this is the chat page!")
