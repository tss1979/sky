import random

POINTS = 10


def change_word(word):
    word_list = list(word.strip().lower())
    word = word.strip().lower()
    random.shuffle(word_list)
    question = ''.join(word_list)
    return word, question


def print_result_message(word, answer):
    if answer == word:
        print(f'Верно! Вы получаете {POINTS} очков')
    else:
        print(f'Неверно! Верный ответ – {word}.')


def count_result(word, answer):
    if answer == word:
        return POINTS
    else:
        return 0


def write_result(name, result):
    with open('history.txt', 'a') as file:
        file.write(f'{name}: {result}\n')


def make_statistic():
    scores = []
    with open('history.txt') as file:
        for line in file:
            scores.append(line.strip().split(' ')[1])
        print(f'Всего игр сыграно: {len(scores)}')
        print(f'Максимальный рекорд: {max(scores)}')


def main():
    result = 0
    print('Введите ваше имя:')
    name = input()
    with open('words.txt') as file:
        for word in file:
            word, question = change_word(word)
            print(f'Угадайте слово: {question}')
            answer = input().strip().lower()
            result += count_result(word, answer)
            print_result_message(word, answer)
        write_result(name, result)
        make_statistic()


main()
