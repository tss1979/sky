import random
from questions import questions


class Question:
    def __init__(self, text, level, answer):
        self.text = text
        self.level = level
        self.answer = answer
        self.is_asked = False
        self.player_answer = None

    def get_points(self):
        '''Метод возвращает количество баллов за правильный ответ на вопрос'''
        return int(self.level) * 10

    def is_correct(self):
        '''Метод проверяет правильность ответа пользователя'''
        return self.answer == self.player_answer

    def build_question(self):
        '''Метод возвращает строку с текстом вопроса в заданном формате'''
        return f'Вопрос: {self.text}\nСложность {self.level}/5'

    def build_positive_feedback(self):
        '''Метод возвращает строку с текстом о правильном ответе пользователя'''
        return f'Ответ верный, получено {self.get_points()} баллов'

    def build_negative_feedback(self):
        '''Метод возвращает строку с текстом о неправильном ответе пользователя'''
        return f'Ответ неверный, верный ответ {self.answer}'


def get_questions():
    '''Функция формирует список объектов вопросов Question из заданного'''
    result = []
    for question in questions:
        result.append(Question(question.get('q'), question.get('d'), question.get('a')))
    return result


def main():
    '''Функция cсодержит основной фунционал игры'''
    questions = get_questions()
    result = []
    while len([x for x in questions if not x.is_asked]) != 0:
        question = random.choice(questions)
        if not question.is_asked:
            print(question.build_question())
            answer = input('Введите ответ: ')
            question.is_asked = True
            question.player_answer = answer.lower()
            if question.player_answer and question.is_correct():
                print(question.build_positive_feedback())
                result.append(question.get_points())
            else:
                print(question.build_negative_feedback())
        else:
            continue
    print(f'Вот и всё!\nОтвечено {len(result)} вопроса из {len(questions)}\nНабрано баллов: {sum(result)}')


main()