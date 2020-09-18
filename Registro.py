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

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Registro = tk.Tk()

filename = PhotoImage(file = "LoginUI.png")
background_label = Label(Registro, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

width_of_window = 450
height_of_windows= 350
LarguraMonitor = Registro.winfo_screenwidth()
AlturaMonitor = Registro.winfo_screenheight()
x_cordinate = (LarguraMonitor/2) - (width_of_window/2)
y_cordinate = (AlturaMonitor/2) - (height_of_windows/2)
Registro.geometry("%dx%d+%d+%d" % (width_of_window, height_of_windows, x_cordinate, y_cordinate))
Registro.title("Registrar")
Registro.minsize(116, 1)
Registro.maxsize(1920, 1080)
Registro.resizable(0, 0)
Registro.update_idletasks()
Registro.overrideredirect(1)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario2 = tk.Entry(Registro)
Usuario2.place(relx=0.330, rely=0.250,height=30, relwidth=0.350)
Usuario2.configure(font="TkFixedFont")
Usuario2.configure(highlightcolor="black")
Usuario2.configure(borderwidth=0)
Usuario2.configure(justify="center")

Senha2 = tk.Entry(Registro)
Senha2.place(relx=0.330, rely=0.480,height=30, relwidth=0.350)
Senha2.configure(font="TkFixedFont")
Senha2.configure(insertbackground="black")
Senha2.configure(borderwidth=0)
Senha2.configure(justify="center")
Senha2.configure(show="*")

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
Sair12.place(relx=0.540, rely=0.725, relheight=0.080, relwidth=0.200)
Sair12.configure(command=Sair2)
Sair12.configure(image=SairBTN2)
Sair12.configure(borderwidth=0)

#----------------Imagem do botão Registro-------------------------------#
RegistroBTN2 = PhotoImage(file="RegistroBN.png")
RegistroBTN = tk.Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro1 = tk.Button(Registro)
Registro1.place(relx=0.320, rely=0.725, relheight=0.080, relwidth=0.200)
Registro1.configure(command=Registrar)
Registro1.configure(image=RegistroBTN2)
Registro1.configure(borderwidth=0)


Registro.mainloop()