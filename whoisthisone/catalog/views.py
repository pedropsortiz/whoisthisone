from django.shortcuts import render, HttpResponse
import wikipedia
from .models import *

wikipedia.set_lang('pt')
search = Person.returnPerson(Person)

def index(request):
    if request.method == 'POST':
        if search.upper() == request.POST['personTest'].upper():
            return render(request, 'index.html', {})
        else:
            raise Exception(search)
    else:
        splitName = search.split(' ')
        try:
            result = wikipedia.summary(search).replace(search, '[...]').replace(splitName[0], '[...]').replace(splitName.remove(), '[...]').split('. ')
        except:
            return HttpResponse("Wrong Input")
        return render(request, 'index.html', {"result": result})
