from  tkinter import *
root = Tk()
root.geometry('550x550')

c = Canvas(root, width= 500, height=500, bg='lightgreen')
c.pack(anchor=CENTER, expand=True)
#====================== Текст ====================
# c.create_text(0, 0,
#               text='Пельмени * 8',
#               font='Arial 20',
#               anchor=NW,
#               fill= 'yellow')
#====================== Текст ====================
# =======================Прямоугольник===================
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill = 'yellow',
#                    width= 10,
#                    outline= 'lime',
#                    )




# =======================Прямоугольник===================
# =======================Многоугольник===================
# c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)




# =======================Многоугольник===================
# =======================Окружность===================
# c.create_oval(50, 10,
#               150, 110,
#               width=9,)

# =======================Окружность===================
# =======================arc===================
# c.create_oval(10, 10, 150, 150, fill= 'grey', outline= 'white')
# c.create_arc(10, 10, 150, 150, fill = 'orange', start=30, extent=-45)
# c.create_arc(10, 10, 150, 150, fill = 'red', start=240, extent=100, style= CHORD)
# c.create_arc(10, 10, 150, 150, fill = 'magenta', start=100, extent=100, style= ARC, width= 10)



# =======================arc===================
# ======================Линия===================
# c.create_line(10, 10, 190, 50, arrow ='both', arrowshape=(50,50,50), width=20)
# c.create_line(100, 180, 100, 60, fill='green', width=5)


# ======================Линия===================
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline='darkred',
#                    dash='-..',
#                    activefill='blue',
#                    activewidth=20)



root.mainloop()