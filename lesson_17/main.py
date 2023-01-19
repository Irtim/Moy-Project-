# spisok = []
# for i in range (1, 6):
#     spisok.append(i)
# print(spisok)
#
# spisok2 = [n for n in range(1, 6)]
# # 1. list comprehension всегда пишется в []
# # 2. for n in range(1, 6) обычный цикл for ->
# # сколько будет элементов в списке
# # 3. всё сто слева от for -> элемент списка
# print(spisok2)

# первый задача
# c2f = lambda c:c * 9/5 + 32
# f2c = lambda f:(f - 32) * 5/9
# c2k = lambda c:c + 273.15
# k2c = lambda k:k - 273.15
# f2k = lambda f:c2k(f2c(f))
# print(c2k(203))

# второй задача
# from random import randint
# siu = lambda zxc: True if zxc == 'Д' else False
# while True:
#     fraza = int(input('сколько кубов бросишь пёс? '))
#     dies = [randint(1, 6) for n in range(fraza)]
#     print(dies)
#     otvet = input('выходишь? (Д/Н) ').upper()
#     siu(otvet)
#     if siu(otvet): # если игрок захотел выйти
#         break
#     else:
#         continue

# тритий задачей
# from random import choice
# chars = [list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫБЭЮЯ'),
#          list('абвгдеёжзийклмнопрстуфхцчшщъьыбэюя'),
#          list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
#          list('abcdefghijklmnopqrstuvwxyz'),
#          list('1234567890')]
#
# cot = [choice(choice(chars)) for n in range(6)]
# cotik = ''.join(cot)
# dictionaryy = {'https://www.google.com':'y86oЯх'}
# ssylka_na_kavkaz = 'https://www.google.com'
# if ssylka_na_kavkaz in dictionaryy:
#     print('Ссылка уже есть в базе, вот ее кот: ')
#     print(dictionaryy[ssylka_na_kavkaz])
# else:
#     print('Ссылка доваблена, держи кота^-^:', cotik)
#     dictionaryy[ssylka_na_kavkaz] = cotik

# четвёртый задачей
u = lambda a, b:a / b
print(u(6,3))

u2 = lambda a, b:a % b
print(u2(6,3))

u3 = lambda a, b:a // b
print(u3(6,3))

u4 = lambda a, b:a ** b
print(u4(6,3))

u5 = lambda a:-a if a < 0 else a #если число отрицательное,
# то меняем знак на противоположный
print(u5(-6))


