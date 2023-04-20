import tkinter as tk
# root = tk.Tk()
# root.geometry('400x400')
# # ======================RADIO BUTTON===================================
# # def get_rb():
# #     print(val_rb.get())
# # val_rb =tk.IntVar()
# # rb = tk.Radiobutton(root, text="РадиоКнопка",
# #                     variable=val_rb,
# #                     value=2,
# #                     command=get_rb())
# #
# # rb.pack()
# # rb1 = tk.Radiobutton(root, text="КанальнаяКнопка",
# #                     variable=val_rb,
# #                     value=3,
# #                     command=get_rb())
# #
# # rb1.pack()
# #
# # ======================RADIO BUTTON===================================
# #
# #
# # ========================SKALA==========================
# # def get_skala(lolkek):
# #     print(skala.get()) # значение либо так
# #     print(lolkek) # либо так
# #
# #
# # skala = tk.Scale(root,
# #                  from_=500, # откуда
# #                  to=1000, # докуда
# #                  width=50, # толщина полоски
# #                  length= 300, # длина полоски
# #                  orient=tk.HORIZONTAL, # оринтация(север)
# #                  tickinterval=100, # подпись
# #                  resolution=50, # шаги
# #                  command=get_skala,)
# # skala.pack()
# # ========================SKALA==========================
# # ===========================KARTINKA=============================
# # img = tk.PhotoImage(file="lyagysh.png" ) # создали объект изображения
# # img = img.subsample(3, 3)
# # img = img.zoom(2, 2)
# # lab = tk.Label(root, image=img)
# # lab.pack()
# #
# # ===========================KARTINKA=============================
# # def switch():
# #     if btn1 ["state"] == 'disabled':
# #         btn1['state'] = "normal"
# #     else:
# #         btn1['state'] = 'disabled'
# #
# #
# # btn1 = tk.Button(root, text='активируй меня',state=tk.DISABLED, fg= 'blue', disabledforeground= 'red', width= 30)
# # btn1.pack(pady=20, ipady=20)
# # btn2 = tk.Button(root, text= 'Активатор3000', command=switch)
# # btn2.pack()
#
#
# ent = tk.Entry(root)
# ent.pack()
# ent.insert(tk.END, 'Перекус таксиста ...')
#
# root.mainloop()
# window = tk.Tk()

# def dream_garden():
#     if bu ['state'] == 'disabled':
#         bu ['state'] = 'normal'
#         bu ['text'] = 'Активен'
#     else:
#         bu ['state'] = 'disabled'
#         bu['text'] = ' не Активен'
#
# cb = tk.Checkbutton(window,
#                     text='Активировать',
#                     command=dream_garden)
# cb.pack()
# # cb.select()
#
#
#
# bu = tk.Button(window,
#                text=' не активен',
#                state=tk.DISABLED)
# bu.pack()
#
# window.mainloop()
root = tk.Tk()
def bold():
    if cb1_val.get(): # tckb cb = True
        lab['font'] += 'bold'
    else:
        lab['font'] -= lab['bold'].replace('bold', '')
#=============================================================================================
def italic():
    if cb1_val.get(): # tckb cb = True
        lab['font'] += 'italic'
    else:
        lab['font'] -= lab['italic'].replace('italic', '')
#=============================================================================================
def overstrike():
    if cb1_val.get(): # tckb cb = True
        lab['font'] += 'overstrike'
    else:
        lab['font'] -= lab['overstrike'].replace('overstrike', '')


# =============================================================================================
def underline():
    if cb1_val.get(): # tckb cb = True
        lab['font'] += 'underline'
    else:
        lab['font'] -= lab['underline'].replace('underline', '')
#=============================================================================================

lab = tk.Label(root,
               text= 'abc',
               font= 'Arial 12')
lab.pack()
#=============================================================================================
cb1_val = tk.BooleanVar()
cb1 = tk.Checkbutton(root,
                    text= 'Жирный',
                    variable= cb1_val,
                    onvalue= True,
                    offvalue= False,
                    command=bold)

cb1.pack()
#=============================================================================================
cb2_val = tk.BooleanVar()
cb2 = tk.Checkbutton(root,
                    text= 'Курсив',
                    variable= cb1_val,
                    onvalue= True,
                    offvalue= False,
                    command=italic)

cb2.pack()
#=============================================================================================
cb3_val = tk.BooleanVar()
cb3 = tk.Checkbutton(root,
                    text= 'Зачёрктнутый',
                    variable= cb1_val,
                    onvalue= True,
                    offvalue= False,
                    command=overstrike)

cb3.pack()
#=============================================================================================
cb4_val = tk.BooleanVar()
cb4 = tk.Checkbutton(root,
                    text= 'Подчёркнутый',
                    variable= cb1_val,
                    onvalue= True,
                    offvalue= False,
                    command=underline)
cb4.pack()



root.mainloop()
