from random import random
import viselica_art as art

print(art.intro)


vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill', 'Artem']

word_answer = random.choice(vocabulary)
word_display = []

for _ in(len(word_answer)):
    word_display.append('_')

print(word_display)
life = 6
counter = 0
letter_is_be = False

while life > 0 and counter != len(word_answer):
    letter = input('Буква:').lower()
    print(art.stages[life])
    letter_is_be = False
    for i in range(len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != '_':
                letter_is_be = True
            else:
                word_display[i] = letter
                letter_is_be = True
                counter += 1
                letter_is_be = True


    if letter_is_be == False:
        life -= 1
        print(word_display)
if counter == len(word_answer):
    print('Пабеда')
else:
    print(art.stages[life])
    print('Не получилось')
    print(word_display)

