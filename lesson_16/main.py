# Словарь
# d = {} # пустой словарь
# d = dict() # пустой словарь
#
#
# d = {'Ключ1': 1,
#      10: "два",
#      True: 'Ложь',
#      True: "Богдан",
#      " ": 0,
#      '': 45,
#      (1, 2, 3): "y"}
# print(d)

# ФУНКЦИИ
# def hellow_orld(): # объявление функции
#      print('Hello world')
#
# hellow_orld() # вызов функции


# def func(imya): # объявление функции с аргументом
#      print(imya, '777')
#
# name = input('Какое погоняло: ')
# func(imya=name) # вызов функции с аргументом


# def slojenie(chislo1, chislo2):
#      result = chislo1 + chislo2
#      return result # return = вернуть что-то из функции
#
# print(slojenie(0, 0)) # вывод результата функции(то что вертнёт return)
# x = slojenie(5, 3)
# print(x)

# def more_5(number):
#      if number > 5:
#           return True
#
# if more_5(8): # если выполнится
#      print('Балдёж')

# 1 задача

# def is_sorted(spisok):
#      s = sorted(spisok)
#      if spisok == s:
#           return  True
#
# spisok = [2, 1, 5, 6, 78, 123]
# if is_sorted(spisok):
#      print('SIIIIUUUUUUUU')
# else:
#      print('я хочу шашлык(')

# 2 задача

# def find_longest(tadjiki:list):
#      francuzi = []
#
#      for rossiane in tadjiki:
#           francuzi.append(len(rossiane))
#      maxim = max(francuzi)
#      portugalci = francuzi.index(maxim) # нашли индекс максимума
#      return tadjiki[portugalci], maxim
#
# uzbeki = ['Россия', 'Пельмени', 'УУУУУУУ']
# print(find_longest(uzbeki))

# 3 задача


# def max_min(spisok):
#      # schweizari = min(spisok)
#      # schotlandzi = max(spisok)
#
#      belorusi = sorted(spisok)
#      italyanci = belorusi[0] # вытащили минимум
#      tayzi = belorusi[-1] # вытащиди максимум
#      return italyanci, tayzi
#
# spisok = [37, 46, 20, 49034, 96]
# print(max_min(spisok))
# 1 задача но она по сути 4

def is_prime(celoe_chislo):
    for vietnamzi in range(2, celoe_chislo + 1):
         if vietnamzi == celoe_chislo: # Мы дошли до конца
            return True
         if celoe_chislo % vietnamzi == 0: # мы нашли делитель
            break

if is_prime(2):
    print('prostoe chislo')
else:
    print('natural chislo')




