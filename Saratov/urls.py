from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Главная/', include('Главная.urls')),
    path('news/', include('news.urls')),
    path('Контакты/', include('Контакты.urls')),
]
