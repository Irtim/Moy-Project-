# Tkinter 3
# import tkinter as tk
#
# win = tk.Tk()
from tkinter import *
from random import randint
from tkinter import messagebox
win = Tk()
win.geometry('700x600')
#=============================1 задача======================================
# Label(win, text='Логин:').grid(row=0, column=0)
# Label(win, text='Пароль:').grid(row=1, column=0)
# Entry(win).grid(row=0, column=1, pady=5)
# Entry(win).grid(row=1, column=1, pady=5)
# btn = Button(win, text='Авторизация').grid(row=2, column=0, columnspan=2, sticky=E)
#===============================================List Box====================================
# def get_lst(pressF):
#     indx = lstbox.curselection()[0]
#     print(lst[indx])
# lst = ['первый', 'второй', 'третий']
# lst_tk = StringVar(value=lst)
# lstbox = Listbox(win, listvariable=lst_tk, selectmode=SINGLE)
# lstbox.pack()
# lstbox.bind('<<ListboxSelect>>', get_lst)
# lstbox['selectbackground'] = 'pink'
# lstbox['selectforeground'] = 'white'
# lstbox['selectborderwidth'] = 10
# for elem in lstbox:
#     lstbox.insert(END, elem)
# btn = Button(win, text='Отправить', command=get_lst)
# btn.pack()
#===============================================List Box====================================
# ===== Верхний блок =====
#===============labelFrame=========
# frame_top = LabelFrame(win, text="Верх")
# frame_top.pack()
# Label(frame_top, width=7, height=4, bg='yellow', text="1").pack()
# Label(frame_top, width=7, height=4, bg='orange', text="2").pack()
#
# # ===== Нижний блок =====
# frame_bottom = LabelFrame(win, text="Низ")
# frame_bottom.pack()
# Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3").pack()
# Label(frame_bottom, width=7, height=4, bg='lightblue', text="4").pack()
#===============labelFrame=========
#====================messagebox=================
# messagebox.showerror('Заголовок1', 'Одна ошибка и ты ошибся')
# messagebox.showinfo()
# messagebox.showwarning()


#====================messagebox=================
#=======================pack===========================
# fr = Frame(win)
# fr.pack(anchor=NW)
# btn1 = Button(fr, text='КЕФТЕМЕ')
# btn2 = Button(fr, text='КЕФТЕМЕ')
# btn2.pack(side=LEFT)
# btn1.pack(side=LEFT)
# btn.pack(anchor=SW, expand= True)
# btn.pack(fill=BOTH, expand=True)


#=======================pack===========================
#=======================GRid===================
# btn1 = Button(win,text='Пацаны1')
# btn1.grid(row=0, column=0)
# btn2 = Button(win,text='Пацаны2')
# btn2.grid(row=0, column=1)
# btn3 = Button(win,text='Пацаны3')
# btn3.grid(row=0, column=2)
# btn4 = Button(win,text='Пацаны4')
# btn4.grid(row=1, column=0,columnspan=3, sticky=E)
# Label(win, text='AAaa').pack()
#=======================GRid===================
#=======================Place===================
# btn1 = Button(win, text='Скибидидобдоб1')
# btn1.place(x=70,y=80)
#=======================Place===================
#=====================After=========================

# def color():
#     btn1['bg'] = 'green'
# def hello():
#     print('print')
#     win.after(1000, hello)
#
# btn1 = Button(win, text='K1')
# btn1.pack()
# win.after(3000, hello)
#=====================After========================


#===============================bind==============
# def func(e):
#     print('ПАЦАНЫ')
#
# btn = Button(win, text='Что-то')
# btn.pack()
# btn.focus_set()
# btn.bind('<u>', func)
#===============================bind==============
#====================================set======================






#====================================set======================
# def move(e):
#     btn.place(x=randint(0, 620), y=randint(0, 520))
#
# btn = Button(win,text='Кто нажал, тот красавчик', bg='gold')
# btn.place(x=10,y=10)
# btn.bind('<Enter>', move)
def blablabla():
    rb_val.set(randint(1, 5))
    win.after(1000, blablabla)

fr = Frame()
fr.pack(anchor=NW)
rb_val = IntVar()
rb1 = Radiobutton(fr, variable=rb_val, value=1)
rb1.pack(side=LEFT)
rb2 = Radiobutton(fr, variable=rb_val, value=2)
rb2.pack(side=LEFT)
rb3 = Radiobutton(fr, variable=rb_val, value=3)
rb3.pack(side=LEFT)
rb4 = Radiobutton(fr, variable=rb_val, value=4)
rb4.pack(side=LEFT)
rb5 = Radiobutton(fr, variable=rb_val, value=5)
rb5.pack(side=LEFT)

blablabla()

win.mainloop()