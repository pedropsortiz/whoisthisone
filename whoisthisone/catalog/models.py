from django.db import models

class Person:
    name_list = ['Alan Turing', 'Albert Einstein', 'Machado de Assis',
            'Adolf Hitler', 'George Orwell',
            'Giancarlo Esposito', 'Leonardo DiCaprio', 'Pedro Álvares Cabral',
            'Luís Inácio Lula da Silva', 'Jair Bolsonaro',
            'Robert Plant', 'Jack, o Estripador', 'Eminem',
            'Gorillaz', 'Dante Alighieri', 'Leonardo da Vinci',
            'Elvis Presley',
            ]

    def returnPerson(self):
        return self.name_list.pop()