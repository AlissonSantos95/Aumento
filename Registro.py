import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle
import reportlab
import pdfkit
import tkinter as tk
import webbrowser
from tkinter import PhotoImage
from tkinter import * 
from tkinter.ttk import *
from win32api import GetSystemMetrics


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Registro = tk.Tk()

width_of_window = 450
height_of_windows= 350
LarguraMonitor = GetSystemMetrics(0)
AlturaMonitor = GetSystemMetrics(1)
x_cordinate = (LarguraMonitor/2) - (width_of_window/2)
y_cordinate = (AlturaMonitor/2) - (height_of_windows/2)
Registro.geometry("%dx%d+%d+%d" % (width_of_window, height_of_windows, x_cordinate, y_cordinate))
Registro.title("Registrar")
Registro.minsize(116, 1)
Registro.maxsize(1920, 1080)
Registro.resizable(1, 1)
Registro.update_idletasks()
Registro.overrideredirect(1)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario2 = tk.Entry(Registro)
Usuario2.place(relx=0.295, rely=0.325,height=30, relwidth=0.400)
Usuario2.configure(background="white")
Usuario2.configure(disabledforeground="#a3a3a3")
Usuario2.configure(font="TkFixedFont")
Usuario2.configure(foreground="#000000")
Usuario2.configure(highlightbackground="#d9d9d9")
Usuario2.configure(highlightcolor="black")
Usuario2.configure(insertbackground="black")
Usuario2.configure(selectbackground="blue")
Usuario2.configure(selectforeground="white")

Senha2 = tk.Entry(Registro)
Senha2.place(relx=0.295, rely=0.525,height=30, relwidth=0.400)
Senha2.configure(background="white")
Senha2.configure(disabledforeground="#a3a3a3")
Senha2.configure(font="TkFixedFont")
Senha2.configure(foreground="#000000")
Senha2.configure(highlightbackground="#d9d9d9")
Senha2.configure(highlightcolor="black")
Senha2.configure(insertbackground="black")
Senha2.configure(selectbackground="blue")
Senha2.configure(selectforeground="white")
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim dos Inputs----------------------------------------------------------------------#
#-----------------------------------------------Inicio das Definições---------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
def Registrar():
     Usuario3 = Usuario2.get()
     Senha3 = Senha2.get()
     msg=tk.messagebox.askyesno("Registro", "Deseja registrar" + Usuario3)
     if (msg):
          pickle.dump(Usuario3, open("dat1.dat", "wb"))
          pickle.dump(Senha3, open("dat2.dat", "wb"))


def Sair2():
    msg=tk.messagebox.askyesno("Sair","Gostaria de sair?")
    if (msg):
          Registro.destroy()

 #------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------fim Definições-----------------------------------------------------------------------------------------------#
#-----------------------------------------------Inicio Botões------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------Imagem do botão login-------------------------------#
SairBTN2 = PhotoImage(file="SairBN.png")
SairBTN = tk.Label(image=SairBTN2)
#-------------Fim Image do botão login-------------------------------#

Sair12 = tk.Button(Registro)
Sair12.place(relx=0.540, rely=0.725, relheight=0.050, relwidth=0.125)
Sair12.configure(activebackground="#ececec")
Sair12.configure(activeforeground="#000000")
Sair12.configure(disabledforeground="#a3a3a3")
Sair12.configure(foreground="#000000")
Sair12.configure(highlightbackground="#d9d9d9")
Sair12.configure(highlightcolor="black")
Sair12.configure(justify='left')
Sair12.configure(text='''Sair''')
Sair12.configure(command=Sair2)
Sair12.configure(pady=20)
Sair12.configure(command=Sair2)
Sair12.configure(image=SairBTN2)
Sair12.configure(borderwidth=0)

#----------------Imagem do botão Registro-------------------------------#
RegistroBTN2 = PhotoImage(file="RegistroBN.png")
RegistroBTN = tk.Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro1 = tk.Button(Registro)
Registro1.place(relx=0.340, rely=0.725, relheight=0.050, relwidth=0.125)
Registro1.configure(activebackground="#ececec")
Registro1.configure(activeforeground="#000000")
Registro1.configure(disabledforeground="#a3a3a3")
Registro1.configure(foreground="#000000")
Registro1.configure(highlightbackground="#d9d9d9")
Registro1.configure(highlightcolor="black")
Registro1.configure(justify='left')
Registro1.configure(text='''Registro''')
Registro1.configure(command=Registrar)
Registro1.configure(pady=20)
Registro1.configure(image=RegistroBTN2)
Registro1.configure(borderwidth=0)


Registro.mainloop()