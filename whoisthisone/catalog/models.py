from django.db import models
import wikipedia
import random
import requests

class Person:
    name = ['Alan Turing', 'Albert Einstein', 'Machado de Assis', 
            'Adolf Hitler', 'Cellbit', 'George Orwell', 
            'Giancarlo Esposito', 'Leonardo DiCaprio', 'Pedro Álvares Cabral',
        ]
    biography = models.CharField(max_length=100)

    def startWikipedia(self):
        random.shuffle(self.name)
        wikipedia.set_lang('pt-br')
        wiki = wikipedia.page(self.name.pop(0))
        requests.Response.close()
        return wiki

    def showBiography(self):
        return self.biography