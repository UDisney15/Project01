"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #include метод.

#Тут ослеживаются переходы по каким либо url адресам. А они уже дальше отслеживают все переходы на другие приложения.
urlpatterns = [
    path('admin/', admin.site.urls), #Функция, метод path. Передается два параметра, первый, который отслеживаем
    #если отслеживается главная страница, то path('') вообще ничего не нужно передавать.
    path('', include('main.urls')) #Путь к главоной странице, path(" ", include('main.urls')) - мы передаем все 
    #полномочия на приложение в main.py. Обращаясь к файлу urls. Нужно добавить этот файл (urls.py) в main.py. 
]
