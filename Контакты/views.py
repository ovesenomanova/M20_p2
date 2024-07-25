from django.http import HttpRequest
from django.shortcuts import render


def Контакты(request: HttpRequest):
    return render(request, 'контакты.html')