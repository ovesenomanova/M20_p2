from django.http import HttpRequest
from django.shortcuts import render


def Главная(request: HttpRequest):
    return render(request, 'главная.html')