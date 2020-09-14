import wx
from wx.lib import sized_controls
ID_Login = wx.NewId()
ID_Registro = wx.NewId()
ID_Sair = wx.NewId()
import simpleaudio as sa
from tkinter import *
import keyboard
from idlelib import window
import webbrowser
import os
url = "https://wwgoogle.com"
import tkinter as tk



window= tk.Tk()

canvas1 = tk.Canvas(window, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (window) 
canvas1.create_window(200, 140, window=entry1)

lbl = Label(window, text="Senha", fg="black", font=("Arial", 23))#texto "bem vindo"
lbl.place(x=145,y=80)# localização na tela do texto "bem vindo"

def getSquareRoot ():
    x1 = entry1.get()
    label1 = tk.Label(window)
    canvas1.create_window(200, 230, window=label1)
    if x1 =="admin":
        window.destroy()
        os.system("Funcoes.py")
button1 = tk.Button(text='Next', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

window.mainloop()