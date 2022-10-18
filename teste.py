import wikipedia
import random

wikipedia.set_lang('en')

class Search:

    name = ['Alan Turing', 'Albert Einstein', 'Machado de Assis', 'Adolf Hitler', 'George Orwell']
    random.shuffle(name)

    def __init__(self, keySearch):
        self.keySearch = keySearch

    def showRequestOfSearch(self):
        return self.keySearch

    def doSearch(self):
        key = Search(str(self.name.pop(0)))
        try:
            resultSearch = wikipedia.summary(key.showRequestOfSearch()).replace('. ', '.\n')
        except:
            print('[...]')
        return resultSearch

print(Search.doSearch(Search).encode('utf8'))