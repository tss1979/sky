from questions import questions
from basic_word import BasicWord
import random
import sys


class App:

    def __init__(self, player):
        self.player = player
        self.word = self.load_random_word()

    @staticmethod
    def load_random_word():
        '''Метод возвращает объект из случайное слово из набора вопросов'''
        word = random.choice(questions)
        return BasicWord(word.get('word'), word.get('subwords'))

    def print_begin_text(self):
        '''Метод выводит приветственные фразы начала игры'''
        print(f'Привет, {self.player.name}!')
        print(f'Составьте {self.word.get_subwords_number()} слов из слова {self.word.word.upper()}')
        print(f'Слова должны быть не короче {self.word.get_min_len()} букв')
        print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
        print('Поехали, ваше первое слово?')

    def print_statistic(self):
        '''Метод печатает статистику игры'''
        print(f'Игра завершена, вы угадали {self.player.get_used_words_quantity()} слов!')

    def check_word(self, users_word):
        '''Метод проверяет соотвествие введенного слова параметрам игры
        и печатает соответствующее предупреждение'''
        if users_word in ['stop', 'стоп']:
            self.print_statistic()
            sys.exit(1)
        elif len(users_word) < self.word.get_min_len():
            print('слишком короткое слово')
        elif users_word in self.player.used_words:
            print('уже использовано')
        elif not self.word.check_input(users_word):
            print('неверно')
        else:
            print('верно')
            self.player.set_used_word(users_word)
