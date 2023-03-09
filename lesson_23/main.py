from random import randint
# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#
#     def __str__(self):
#         print('Ы')
#         return 'Я Кристина'
#
# eugenii = Person("Юджин", 40)
# anna = Person(vozrast=0, imya='Кристина')
#
# print(anna.name)
# print(eugenii.age)
#
# print(anna)
#
#
# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимания, что здесь нет print(), просто обращение по ключу
# hi[42]
# hi['Movavi']

#1задача
#
# class Person:
#         def __init__(self, imya, vozrast, family):
#             self.name = imya
#             self.age = vozrast
#             self.family = family
#             self.grades = [randint(2, 5) for n in range(randint(5, 10))]
#             self.sa = sum(self.grades) / len(self.grades)
#         def __str__(self):
#             return f'{self.name} {self.age} {self.family}'
#         def greet(self):
#             return f'Привет! Я {self.name} мне {self.age} я {self.family}'
#
#
#
# anna= Person('Аня', 20, 'Милашкаrrrr' )
# artem = Person('Тёма', 14, 'Попенин')
# BUSTER = Person('Слава', 24, 'Бустеренко')
# anton = Person('Антон', 20, 'Смирнов')
# studen = [anna, artem, anton, BUSTER]
#
# dnevnik = {}
# for item in studen:
#     dnevnik[item.name] = item.sa
#
#
# sorted_dnevnik = dict(reversed(sorted(dnevnik.items(), key=lambda item: item[1])))
#
# schetchik = 0
# for item in sorted_dnevnik:
#     schetchik += 1
#     print(f'{schetchik}. {item} - {sorted_dnevnik[item]}')
# print(anna.greet())
# print(anna.family)
# print(anna.name)
# print(anna.age)
# print(anna.grades)
# print(anna.sa)
# print(anna)
#2 задачаt()
class Buster:
    def __init__(self, d1, d2):
        self.dot1 = d1
        self.dot2 = d2
    def ploshad(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return a * b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

dot1 = Point(1, 152)
dot2 = Point(2, 250)
bolshoy_kvadrat = Buster(dot1, dot2)

print(bolshoy_kvadrat.ploshad())