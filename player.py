class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def get_used_words_quantity(self):
        '''Метод возвращает количество угаданных слов'''
        return len(self.used_words)

    def set_used_word(self, word):
        '''Метод добавляет слово в список использованных(угаданных) слов'''
        self.used_words.append(word)