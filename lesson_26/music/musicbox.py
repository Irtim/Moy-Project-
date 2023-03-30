# import random
# import playsound
# class MusicBox:
#     def __init__(self):
#         self.variants = 'yge' # варианты угадыванных звуков
#         self.score = 0 # Счёт Очков
#         self.sequence = random.choice(self.variants) # Последовательность
#     def __next(self):
#         dlina = len(self.sequence) + 1 # прибавляем к длине
#         self.sequence = ''
#         for _ in range(dlina):
#             self.sequence += random.choice(self.variants)
#
#     def chek(self, otvet):
#         if otvet == self.sequence:
#             playsound.playsound('sounds/pravilno.wav')
#             self.__next()
#             self.score += 1
#         else:
#             playsound.playsound('sounds/NePravilno.wav')
#             self.score -= -5
#     def igraem(self):
#         for bukva in self.sequence:
#             playsound.playsound(f'sounds/{bukva}.mp3')



