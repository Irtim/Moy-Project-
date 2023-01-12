# 1 задача

# phrase = "РОССИЯ, РОССИЯ, РОССИЯ И БОГДАН! ".title()
# print(phrase)
# symbols = list("!@#$%^&*()1234567890<>,.?") # \" - экранирование
# phrase_clear = ""
# for ovoshi in phrase:
#     if ovoshi not in symbols:
#         phrase_clear += ovoshi
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
#
#
# d = {}
# for dom in phrase_list:
#     if dom in d:
#         d[dom]
#     else:
#         d[dom] += 1
# print(d)
# 2 задача
# sloj = 0
# d = {'Молоко': 100,
#      'Доширак': 21,
#      'Чипсы': 0.5,
#      'Богдан': 999}
# for i in d.values(): # перебор по значениям
#     sloj = sloj + i
# print(sloj)

# 3 Задач
# die_sides = 6
# die_count = 2
# d = {}
#
# for first in range(1, die_sides + 1):
#     for second in range(1, die_sides + 1):
#         if first + second not in d:
#             d[first + second] = [(first, second)]
#         else:
#             d[first+second].append((first, second))
#
#
# # вывод
# for tadjikistan in d:
#     print(f'{tadjikistan}: {d[tadjikistan]}')






