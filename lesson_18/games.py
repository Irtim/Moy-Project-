import easygui
import random

def rock_paper_scissors():]
    otvets = {'BUMAGA':'img/BUMAGA.png',
            'NOZNICI':'img/NOZNICI.png',}
    easygui.buttonbox(
        msg='Выбери элемент',
        title='KAMEN V POCHKAX',
        images=['img/BUMAGA.png', 'img/NOZNICI.png', 'img/CAMEN.png'],
        choices=('ББ', ),


    )


def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()