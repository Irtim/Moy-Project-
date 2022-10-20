# # a = input("Фамилия: ")
# # b = input("Имя: ")
# # c = input("Отчество:")
# # print(a.title(), b.title()[0], ".", c.title()[0], ".")
#
# # a = "Привет, меня зовут"
# # print(a.split(",")[0])
#
# # a = input("Твои слова :")
# # print(a.split(" ")[1:])
#
# # a = input("Твои слова: ")
# # print(a.split(" ")[:-1])
#
# # a = input("Строка: ")
# # b = input("Слово: ")
# # c = input("Слово:")
# # print(a.replace(b, c))
#
# # a = input("Строка: ")
# # print(a.replace("е", "ё"))
#
# # a = input("Ваша почта: ")
# # print(a.split("@")[0])
# # print(a.split("@")[1])
#
# # a = input("Строка: ")
# # print(a.replace("!", " "))
#
# # a = input("Строка: ")
# # print(a.split("!")[-2])
#
# # a = input("Строка: ")
# # print(a.split("!")[0])
#
# #a = input("Строка: ")
# #print(a.replace("о", "@")[-6, -2])
# # # Списки
# # name_1 = 'Toxa'
# # name_2 = 'AHTOH'
# # name_3 = 'AHTyAH'
# # mega_anton = [name_3, name_2, name_1] #С писок
# # # операция со спискоm
# # mega_anton.append('Toшa') # добавить элемент в список
# # print(mega_anton)
# # mega_anton.pop(2) # удалить во индексу
# # mega_anton.remove('Toxa') # удалить по значения
# # print(mega_anton)
#
# # Индексация несколько раз
# # man = [['Антон', 'Гриша'],['Компьютеры', 'Настолки'],'Мама']
# # print(man[0][1]) # вывести Гришу
# # number = int(input('Введи число:'))
# # if number < 0:
# #     print('Отрицательное')
# # elif number > 0:
# #     print('Положительное')
# # else:
# #     print("Ноль")
# # year = int(input("Введи год:"))
# # if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
# #     print("Високосненько😀")
# # else:
# #     print("Не високосненько😓")
# #number_1 = int(input("Первое число: "))
# # operation = input("Введи операцию (+, -, *, /): ")
# # number_2 = int(input("Второе число: "))
# #
# # lst = ['+',' -', '*', '/']
# # if operation in lst:
# #     if operation == "+":  # если сложить
# #          print(number_1 + number_2)
# #     elif operation == "-":  # если вычесть
# #         print(number_1 - number_2)
# #     elif operation == "/":  # если делить
# #          print(number_1 - number_2)
# #     else:  # иначе(умножить)
# #          print(number_1 * number_2)
# # else:
# #     print("Написал фигню")
# # number_1 = int(input("Первое число: "))
# # number_2 = int(input("Второе число: "))
# # number_3 = int(input("Третье число: "))
# #
# # lst = [number_3, number_2, number_1]
# # print('Максимальное число:', max(lst))
# # print('Минимальное число:', min(lst))
# #ticket = input('Введи номер билета: ')
# if len(ticket) == 6 and ticket.isdigit():
#     first_half = ticket[:3]
#     last_half = ticket[-3]
#     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     last_sum = int(last_half[-3]) + int(last_half[-2]) + int(last_half[-1])
#     if first_sum == last_sum:
#         print("Билет счастливый🎟:")
#     else:
#         print("Game Over💔:")
# else:
#     print('Фигню написал💩')
#                                             'УРОК ЗАКОНЧИН'