# Фуркции
# def functia(x):# объявление фенкции
#     return x + 1
#
# print(functia(5)) # вызов функции
#
# f = lambda x2: x2 + 1 # ообъявление лямда функции
# print(f(5)) # вызов лямда функции

# фасольная задача

# beans = 20
# def fludd(x):
#     global beans
#     beans -= x
#     while beans <= 0:
#         while True:
#             vtoroi_player = int(input('Второй игрок:Сколько фасоли взять?: '))
#             if vtoroi_player < 4 and vtoroi_player > 0:
#                 break
#     fludd(x)
#     print(beans)
# while beans <= 0 :
#     while True:
#         first_player = int(input('Первый игрок:Сколько фасоли взять?: '))
#         if first_player < 4 and first_player > 0:
#             break
#     fludd(first_player)
#     print(beans)
# Стрелок
# import time
# from random import randint
# print('Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь СТРЕЛЯЙ, у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.')
#
# input('нажми Enter чтобы начать...')
# print('Время пострелять')
# time.sleep(randint(2, 5))
# start = time.time()
# print('СТРЕЛЯЙ!!!')
# end = time.time()
# delta = end-start
# print(delta)
# if delta > 0.3:
#     print('Ты медленный черепаха🥱!! Стреляй быстрее!!😎')
# elif delta < 0.01:
#     print('Ты быстр 😮😮')
# else:
#     print('Победа 🍕')



