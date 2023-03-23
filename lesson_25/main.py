# Классы. Решение кейса
# class Eshekere:
#     pi = 3.14 # public статичный
#     __city = 'Новосибирск' # private статичный
#     def __init__(self):
#         self.hi = 180 # public динамический
#         self.__vozrast = 40 # private динамический
#
#
# obj = Eshekere()
# print(obj.hi)
# print(Eshekere.pi)


# class Chelovek:
#     def __init__(self, height=200): # значение по умолчанию
#         self.hi = height
#
# obj = Chelovek() # не передал --> по умолчанию
# print(obj.hi)
#
# obj = Chelovek() # передал -> переданный аргумент
# print(obj.hi)

from  random import randint
class Human:
    default_name = 'Григорий'
    default_age = 18
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 10.000
        self.__house = None

    def info(self):
        return (self.name, self.age, self.__money, self.__house)

    def earn_money(self):
        self.__money += 2

    def default_info(self):
        return (self.default_name, self.default_age)

    def __make_deal(self, dom):
        if  self.__money > dom.final_price():
            self.__money -= dom.final_price()
            return True
        else:
            if self.__money < dom.final_price():
                return False



    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__house = dom
            return  'Хатф приобретена'
        else:
            return 'У тебя:NN. нужно: MM'
class House:
    def __init__(self, area='krasiva', price=100.000):
        self.__area = area
        self.__price = price
        self.__skidOCHKA = randint(5, 25) / 10

    def final_price(self):

        return self.__price - self.__price * self.__skidOCHKA

artem = Human()
dom = House()

artem.buy_house(dom)



