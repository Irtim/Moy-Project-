from tkinter import *

win = Tk()
win.geometry('1600x900')
#
#
# def poop():
#     global timer
#     c.delete('all')
#     timer += 1
#     c.create_image(300, 250, image=img)
#     c.create_text(300, 255, text=timer, font='Arial 25')
#     c.after(1000, poop)
#     if timer == 16:
#         win.destroy()
#
# img = PhotoImage(file='CHASI.png').subsample(4, 4)

c = Canvas(win, width=600, height=500, bg='silver')
c.pack(anchor=CENTER, expand=True)
# timer = 0
#
# poop()
c.create_text(10, 10, anchor=NW, text='Школа', font='Arial 25')
c.create_line(150, 25, 250, 25, arrow='last')
c.create_text(300, 10, anchor=NW, text='Туда-Сюда', font='Arial 25')
c.create_line(350, 25, 600, 25, arrow='last')
c.create_text(600, 10, anchor=NW, text='успех', font='Arial 25')
c.create_line(350, 25, 600, 25, arrow='last')
win.mainloop()