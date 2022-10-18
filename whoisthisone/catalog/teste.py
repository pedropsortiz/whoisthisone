import wikipedia

wikipedia.set_lang('en')

class Search:

    def __init__(self, chave):
        self.chave = chave

    def showSearch(self):
        return self.chave

    def wikipediaFunction(key):
        try:
            print(wikipedia.summary(key.showSearch()).replace('. ', '.\n'))
        except:
            print('[...]')

Search.wikipediaFunction(Search(str('Albert Einstein')))