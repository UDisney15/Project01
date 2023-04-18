from django.shortcuts import render #при помощи рендера можно показывать какой html шаблон будет показан, когда 
#пользователь перейдет на ту или другую страницу браузера.
from django.http import HttpResponse #класс ответа
# Create your views here.

def index(request): #метод, внутри ничего нет, поэтому прописывается pass. Но если происходит действие,
	#то нужен хотя бы один параметр (request)- другими словами запрос.
	return render(request, 'main/index.html') #request первый параметр передаваемый из переменной. Второй параметр название html шаблона страницы.



def about(request): #метод, внутри ничего нет, поэтому прописывается pass. Но если происходит действие,
	#то нужен хотя бы один параметр (request)- другими словами запрос.
	return render(request, 'main/about.html')
