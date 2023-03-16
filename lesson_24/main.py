# # class Nazvanie:
# #     def __init__(self):
# #         self.money = 1_000 # Без __ публичный
# #         self.__zarplata = 2 # С __ приватная
# #
# #     def bar(self): # публичный метод
# #         if self.__zarplata > 4: # Используем приват
# #             return True
# #         else:
# #             self.__sad() # вызов приват метода
# #             return False
# #
# #     def __sad(self): # приват метод
# #         print('Саня хочет бухать')
# #
# #
# #
# # sanya = Nazvanie()
# # print(sanya.money)
# # sanya.money += 100 # Изменить или добавить
# # # sanya.__zarplata = 10 # публичный
# # # print(sanya.__zarplata) # Приват нельзя выводить
# # # sanya.__zarplata =+ 10 #  публичный но нельзя изменять
# # # print(sanya.__zarplata)
# #
# # sanya._Nazvanie__zarplata = 1_000_000 # Изменяем приват, при спомощи _название класса
# # print(sanya.bar())
# # class Car:
# #     def zavod(self):
# #         print('«Автомобиль заведен»')
# #
# #     def konew(self):
# #         print('«Автомобиль заглушен»')
# #
# #     def age(self):
# #         self.God = 2009
# #
# #
# #     def type(self):
# #         self.tipe = 'Volsebniy'
# #
# #
# #     def wdtn(self):
# #         self.wdtn = 'Zelen'
# #
# # print(self.zavod)
# # print(self.konew)
# # print(self.God)
# # print(self.tipe)
# # print(self.wdtn)
# import string
# import datetime
# # 2 задача
# # class Alphabet:
# #     def __init__(self, lang):
# #         self.__lang = lang
# #         self.__letter = string.ascii_lowercase
# #     def print(self):
# #         print(self.__letter)
# #     def letters_nums(self):
# #         print(len(self.__letter))
# # al = Alphabet('eng')
# # al.print()
# # al.letters_nums()
# # 3 задача
# class Vrema:
#     def __init__(self):
#         # self.__time = datetime.datetime.now().strftime('%H:%M:%S')
#         self.__time =
#         self.__h, self.__m, self.__s = self.__time.split(':')
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#         # self.m = self.__time.split(':')[1]
#         # self.s = self.__time.split(':')[2]
#
#     def hours(self):
#         self.__h += 1
#     def minutes(self):
#         self.__m += 1
#     def secunds(self):
#         self.__s += 1
#     def test_h(self):
#         if self.__h > 23:
#             self.__h = 0
#     def test_m(self):
#         if self.__m > 59:
#             self.__m = 0
#             self.__h += 1
#     def vivod(self):
#            print(f'{str(self.__h).rjust(2, '0')}:{self.__m}:{self.__s}')
#
# time_1 = Vrema()
# time_1.minutes()
# time_1.test_m()
# time_1.vivod()


