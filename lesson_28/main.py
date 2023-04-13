# import tkinter as tk
#
# def baget(event):
#     print('Я круассон')
#
#
#
# window = tk.Tk() # создание,иницилизация
# window.geometry('500x400') # размеры по иксу и игрику
# window.title('окно')
#
# btn = tk.Button(window, text='ЫЫЫЫ') # создание кнопки
# btn.pack() # Размецение кнопки
# btn['text'] = 'zazazaza' # изменение конфигурации
# btn['font'] = ('Arial Black', 14,
#                'bold', # жирный
#                'underline', # подчеркнутый
#                'italic', # курсив
#                'overstrike',#  зачеркнуть
#      -           )
# btn['bg'] = 'orange' # цвет фона
# btn['fg'] = "white" # цвет текста
# btn['width'] = 15 # width = ширина
# btn['height'] = 2 # height = высота
# # btn['borderwidth'] = 15 # ширина рамки
# btn['bd'] = 15 # Ширина рамки
# # btn['command'] = baget # нажатие левой кнопкой
# btn.bind('<Double-Button-1>', baget)
#
#
# window.mainloop() # отображение окна в КОНЦЕ