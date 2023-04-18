from django.urls import path
from . import views
#Тут ослеживаются переходы по каким либо url адресам. А они уже дальше отслеживают все переходы на другие приложения.
urlpatterns = [
    path('', views.index), #('')начальная страница не индексируется.
    path('about', views.about)

]
