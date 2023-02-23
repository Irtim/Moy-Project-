# try:
#     number = int(input('Введи число: '))
# except ValueError:
#     print('Понял')
# else: # если исключения не найдены
#     print('Понял2')
# finally: # работакт в любом
#     print('Я поработав')


# name = input('Введи имя друга(собаки): ').title()
# try:
#     if name == 'Артём':
#         raise ValueError('Не брат ты мне, гнида черножопая')
# except ValueError as Pelmeni:
#     print(Pelmeni, 'Запрещаю')

# 1 задача
#
# def masha(content):
#     s = 0
#     k = 0
#     for chiselko in content:
#         try:
#             s += int(chiselko)
#         except ValueError:
#                 print('Ты чо пёс? Не ломай',  chiselko)
#         else:
#                 k += 1
#         if k == 0:
#             print('Чисел не было найдено')
#             return # Выход из функции
#     return round(s / k, 3)
# try:
#     g = open('23.txt', 'r', encoding="utf-8")
# except FileNotFoundError:
#     print('Файла нет')
#     quit() # выход
# content = g.read().split() # по пробелам и переносом строки
# g.close()
# print(masha(content))
# 2 задача
# try:
#     g = open('23.txt', 'r', encoding="utf-8")
# except FileNotFoundError:
#     print('Файла нет')
#     quit() # выход
# content = g.readlines()
# g.close()
# print(content)
#
#
# for i, student in enumerate(content):
#     content[i] = student.split()
#
# maxi = -1
# for student in content:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print('Неверно указаны баллы', student)
#     except IndexError:
#         print('Баллы отсутствуют', student)
# if maxi == -1:
#     print('Нету файла')
#     quit()
# print(maxi)
# 6 задача
try:
    g = open('23.txt', 'r', encoding="utf-8")
except FileNotFoundError:
     print('Файла нет')
     quit() # выход

content = g.read()
word = input('какое слово мы ищем:')
print(content.count(word))
