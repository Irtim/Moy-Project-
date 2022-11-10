# # ЦИКЛЫ
# # While (пока)
# #x = 10
# #while x != 0: #пока x не равен нулю
# #    print(x)
# #    x -=1 # то же самое, что и x = x - 1
# #
# #while True: # срабатывает каждый раз
# #    break # выйти из while или его остановить
#
# # for
# # lst = ['А', 'Б', 'В', 'Г', 'Д',]
# #for letter in lst: # проитерироваться по списку
# #    print(letter)
# #
# #for i in range(0, 4):
# #    print(i)
# #word = input('Введи словечко: ')
# #while word: # пока слово не пустое(из-за типа 'Строчки'
# #    print(word, end=' ')
# #    word = word[:-1]
#
# # number = int(input("Введи число: "))
# # while number: # пока number != 0 (из-за типа "число)
# #     number -= 1
# #     if number % 2 == 0:
# #          print(number, end=" ")
# x = input("Введи число: ").strip()
# if not x.isdigit() or int(x)<=1:
#     print('Одна ошибка и всё')
#     quit()
#
# else:
#     x = int(x)
#
# step = 0
# while x != 1:
#     step += 1
#     if x % 2 == 0:
#         print(f"{step})", end=' ')
#         print(x, "/ 2 =", end=" ")
#         x = x // 2
#     else:
#         print(f"{step})", end=" ")
#         print(x, "* 3 + 1 =", end=" ")
#         x = x * 3 +1
#     print(x)
# print('Шагов:', step)
