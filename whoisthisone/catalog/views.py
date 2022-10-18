from django.shortcuts import render, HttpResponse
import wikipedia
from .models import *

wikipedia.set_lang('pt')


def index(request):
    search = Person.name.pop()
    teste = search.split(' ')
    try:
        result = wikipedia.summary(search).replace(search, '[...]').replace(teste.pop(), '[...]').split('. ')
    except:
        return HttpResponse("Wrong Input")
    return render(request, 'index.html', {"result": result})
