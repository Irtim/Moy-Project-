import random
import requests
class User:
    def __init__(self):
        self.__lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales porta vehicula. Morbi sapien elit, hendrerit non turpis at, consectetur porttitor nibh. Mauris malesuada eros nec dui facilisis, a feugiat magna tempus. Aenean malesuada ex sem, a volutpat ipsum varius sit amet. Donec cursus imperdiet sem, ut egestas est porta vitae. Aliquam nec libero dolor. Donec in quam commodo, placerat.'
        self.__data = requests.get('https://api.randomdatatools.ru/').json()
        self.login = self.__data['Login']
        self.__password = self.__data['Password']
        self.imya = self.__data['FirstName']
        self.familiya = self.__data['LastName']
        self.posts = [self.__lorem[random.randint(0, 35):random.randint(36, 70)]]


