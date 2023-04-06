# Задача с Земликопами
# zemlekopi = 1.01
# a = (round(zemlekopi))
# print(a)

# 1 задача
# perviy_color = input('Введите первый цвет: ').lower().strip()
# vtoroi_color = input('Введите второй цвет: ').lower().strip()
# color = ('красный', 'синий', 'жёлтый', )
# if perviy_color not in color or vtoroi_color not in color:
#     print('Неправильно')
# elif (perviy_color == color[0] and vtoroi_color == color[2])\
#         or (perviy_color == color[2] and vtoroi_color == color[0]):
#     print('Оранжевый')
# elif (perviy_color == color[2] and vtoroi_color == color[1])\
#         or (perviy_color == color[1] and vtoroi_color == color[2]):
#     print('Зелёный')
# elif (perviy_color == color[0] and vtoroi_color == color[1])\
#         or (perviy_color == color[1] and vtoroi_color == color[0]):
#     print('Фиолетовый')
# else:
#     print(perviy_color.capitalize())
# 2 задача

print(int('08'))

start = input('Начало первого урока (чч:мм):' )
urok = int(input('Длительность урока (мин): '))
peremen = int(input('Длительность перемен (мин): '))
n = int(input('На сколько уроков нужно расписание: '))

splited_start = start.split(':')
hours = int(splited_start[0])
minutes = int(splited_start[1])
vremya = hours * 60 +minutes

for i in range(4100):
    print(i + 1, 'Урок:' , end='' )
    print(f'{str(vremya//60).rjust(2, "0")}:{str(vremya%60).rjust(2, "0")} - ', end='')
    vremya += urok
    print(f'{str(vremya//60).rjust(2, "0")}:{str(vremya%60).rjust(2, "0")} - ', end='')
    vremya += peremen