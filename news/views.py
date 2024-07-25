from django.http import HttpRequest
from django.shortcuts import render


def news(request: HttpRequest):
    return render(request, 'news.html')