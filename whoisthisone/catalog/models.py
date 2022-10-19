from django.db import models

class Person:
    name_list = ['Alan Turing', 'Albert Einstein', 'Machado de Assis',
            'Adolf Hitler', 'Cellbit', 'George Orwell',
            'Giancarlo Esposito', 'Leonardo DiCaprio', 'Pedro Álvares Cabral',
            'Luís Inácio Lula da Silva', 'Jair Bolsonaro',
            'Robert Plant', 'Jack, o Estripador', 'Eminem',
            ]

    def returnPerson(self):
        return self.name_list.pop()