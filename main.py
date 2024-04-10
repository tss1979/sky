from player import Player
from app import App


def main():
    name = input('Ввведите имя игрока: \n').title()
    player = Player(name)
    app = App(player)
    app.print_begin_text()
    while len(app.word.subwords) != player.get_used_words_quantity():
        users_word = input('Введите слово: ').lower()
        app.check_word(users_word)
    app.print_statistic()



main()
