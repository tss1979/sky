class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.word

    def check_input(self, word):
        '''Метод проверяет наличие введенного пользователем слова в списке правильных ответов'''
        return word in self.subwords

    def get_subwords_number(self):
        '''Метов возвращает количество загаданных слов'''
        return len(self.subwords)

    def get_min_len(self):
        '''Метод возвращает минимальное количество букв из которых должно состаять слово - ответ'''
        return min([len(x) for x in self.subwords])






