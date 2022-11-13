from tkinter import *
from tkinter import ttk

import model
root = None
frm = None

def createMenu():
    global root
    global frm
    root = Tk()
    root.title('Телефонный справочник')
    frm = ttk.Frame(root, padding=15)
    frm.grid()
    ttk.Label(frm, text='Добро пожаловать в справочник\n').grid(column=1, row=1)
    ttk.Button(frm, text="Вывести справочник", command=printTel).grid(column=0, row=6)
    ttk.Button(frm, text="Выгрузить в book.html", command=saveHTML).grid(column=2, row=6)
    ttk.Button(frm, text="Добавить запись(через консоль)", command=addTel).grid(column=0, row=7)
    ttk.Button(frm, text="Выгрузить в book.xml", command=saveXML).grid(column=2, row=7)
    ttk.Button(frm, text="Выход", command=root.destroy).grid(column=1, row=8)
    root.mainloop()


def printTel():
    global frm
    ttk.Label(frm, text=f'{model.printTel()}').grid(column=0, row=2)

def saveHTML():
    global frm
    a = ttk.Label(frm, text=f'{model.saveAsHTML()}').grid(column=0, row=3)  

def saveXML():
    global frm
    a = ttk.Label(frm, text=f'{model.saveAsXML()}').grid(column=0, row=4)  

def addTel():
    global frm
    ttk.Label(frm, text=f'{model.addTel()}').grid(column=0, row=5)  


