# import random
#
# game = 'y'
# while game == 'y':
#     card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     hand_player = [random.choice(card)]
#     hand_computer = [random.choice(card)]
#     score_player = 0
#     score_computer = 0
#     get_card = 'y'
#     while get_card == 'y':
#         hand_player.append(random.choice(card))
#         if sum(hand_player) > 21 and  11 in hand_player:
#             for i in range(0, len(hand_player)):
#                 if hand_player[i] == 11:
#                     hand_player[i] = 1
#                     break
#         score_player = sum(hand_player)
#         print(f"Твоя рука: {hand_player}. Очков: {score_player}")
#         print(f"Первая карта компутера: {hand_computer[0]}")
#
#         if score_player > 21:
#             get_card = 'n'
#         else:
#             get_card = input('Берём карту? y - да, n - нет:')
#
#     while sum(hand_computer) < 17:
#         hand_computer.append(random.choice(card))
#         if sum(hand_computer) > 21 and  11 in hand_computer:
#             for i in range(0, len(hand_computer)):
#                 if hand_computer[i] == 11:
#                     hand_computer[i] = 1
#                     break
#
#     score_computer = sum(hand_computer)
#     print('=' * 10)
#     print(f'Твоя рука: {hand_player}. Очков: {score_player}.')
#     print(f'Рука диллера: {hand_computer}. Очков: {score_computer}.')
#
#     if score_player > 21 and score_computer > 21:
#         print("Перелёт у обоих. Ничья.")
#     elif score_player > 21:
#         print("Твой перелёт. Ты проиграл.")
#     elif score_computer > 21:
#         print("Перелёт компьютера. Ты победил.")
#     elif score_player == score_computer:
#         print("Ничья")
#     elif score_player > score_computer:
#         print("Победа.")
#     else:
#         print("Проиграл")
#
#     game = input("Играем дальше? y - да, n - нет:")



