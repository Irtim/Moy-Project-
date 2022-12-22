# s = set()
# s1 = {1, 2, 3, 3}
# print(s1)

# s2 = {'А', 'Б', 'В'}
# print(s2)

# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# print(s1 | s2)
#
# print(s1.intersection(s2))
# print(s1 & s2)
#
# print(s1.difference(s2))
# print(s1 - s2)
#
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)
#
#
# # словарь
# d = {}
# d1 = {'Пи': 3.14, 'Преполаватель': 'Антон',
#       'Список дел': ['ВЫЖИТЬ', 'Ловить балдёж'],
#       'Словарь': {"Вл1": 1}}
# print(d1['Преполаватель'])
# print(d1['Список дел'])
# print(d1['Словарь']['Вл1'])
# 1 задача
# from random import randint
#
# lst = []
#
# for i in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst)
# print(unique)
#
# print(f'{len(unique)} штук: {unique}')
# 2 задача
# from random import randint
#
# lst1 = []
# lst2 = []
#
# size = randint(100, 1000)
# r_start = 0
# r_end = 10_000 # _ не на что не влияет
#
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
# set1 = set(lst1)
# set2 = set(lst2)
#
# inter = set1.intersection(set2)
# print(f'Общих чисел: {len(inter)}')
# print(f'[Кол-во генераций]: {size}')
# print(f'[Минимальное значение]: {min(inter)}')
# print(f'[Максимальное значение]: {max(inter)}')
# возможное решение,но колхозное
# inter1 =list(inter)
# inter1.sort()
# print(inter1)
# print(sorted(inter))
# 3 задача
# set1 = set()
# insert = ''
# while insert != 'end':
#     insert = input('Ввод: ')
#     if insert.lstrip('-').isdigit():
#         if insert not in set1:
#             print('❌ HET')
#             set1.add(insert)
#         else:
#             print('ДА ✅')
#     elif insert == 'end':
#         break
#     else:
#         print('Число хочу❗❗')



