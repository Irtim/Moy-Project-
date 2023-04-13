import tkinter as tk

# def show_message():
#     # приём значения из Entry
#     message = ent.get()  # получить занчение
#     ent.delete(0, 'end')  # очистка поля для ввода полностью
#     lab['text'] = message
#     print(message)
#
#     # приём значения из Txt
#     message2 =txt.get(0.0, 'end') # отсчёт от 1.0
#     txt.delete (1.0, 'end') # очистка текста
#     print(message2)
#
#
# window = tk.Tk()
# window.geometry('300x400')
# lab = tk.Label(window, text='Бублики', font='Verdana 18 bold italic', fg='black', bg='red4', width= 50) # Надпись
#
# lab.pack()
# ent = tk.Entry(window , bd=10, width= 20) # поле для ввода
# ent.pack()
#
# btn = tk.Button(window, text='отправить', fg='black', bg='red4', font='Verdana 18 bold italic', command=show_message)
# btn.pack()
#
# txt = tk.Text(window, width=20, height= 5) # многострочный ввод
# txt.pack()
#
#
# window.mainloop()
def snow_message():
    message = ent.get()
    ent.delete(0, 'end')
    massage = txt.get()
    txt.delete(0.0 , 'end')

window = tk.Tk()
window.geometry('400x500')

add = tk.Label(window, text='Вад адрес:', font='Verdana 18 bold italic', fg='white', bg='lightblue', width= 50)
add.pack()

ent = tk.Entry(window , bd=10, width= 30)
ent.pack()

com = tk.Label(window, text='Коментарий:', font='Verdena 18 bold italic')
com.pack()


txt = tk.Text(window, width=20, height= 5)
txt.pack()

btn = tk.Button(window, text='отправить', fg='White', bg='lightblue', font='Verdana 18 bold italic',command = snow_message)
btn.pack()

window.configure(background='grey')
window.mainloop()