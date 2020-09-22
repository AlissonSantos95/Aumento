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
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação dO db-------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#criar o server


#criar a mesa


#DATATYPES:
#REAL (NUMEROS COMO 1,5-1,6-1,7
#TEXT (APENAS TEXTO)
#INTERGER(NUMEROS INTEIROS COMO 1,2,3,4,5,6)
#BLOB (PODE ARMAZENAR IMAGENS
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim DO SERVER-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Registro = tk.ThemedTk()
Registro.get_themes()
Registro.set_theme("plastik")


#filename = PhotoImage(file ="LoginUI.png")
#background_label = Label(Login, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)


width_of_window = 412
height_of_windows= 460
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

w = Canvas(Registro, bg="grey", width=290, height=320)
w.place(x=63, y=70)

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario2 = Entry(Registro)
Usuario2.place(x=110, y=150, height=28, width=205)
Usuario2.configure(font="TkFixedFont")
Usuario2.configure(justify="center")

Senha2 = Entry(Registro)
Senha2.place(x=110, y=240, height=28, width=205)
Senha2.configure(font="TkFixedFont")
Senha2.configure(show="*")
Senha2.configure(justify="center")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim dos Inputs----------------------------------------------------------------------#
#-----------------------------------------------Inicio das Definições---------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
def RegistrarB():
     Usuario3 = Usuario2.get()
     Senha3 = Senha2.get()
     msg=messagebox.askyesno("Registro", "Deseja registrar" + Usuario3)
     if (msg):
          pickle.dump(Usuario3, open("dat1.dat", "wb"))
          pickle.dump(Senha3, open("dat2.dat", "wb"))
          Registro.destroy()
def Sair2():
    msg=messagebox.askyesno("Sair","Gostaria de sair?")
    if (msg):
           Registro.destroy()
          

 #------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------fim Definições-----------------------------------------------------------------------------------------------#
#-----------------------------------------------Inicio Botões------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------Imagem do botão login-------------------------------#


Registrar    = Button(Registro)
Registrar.place(x=77, y=310, relheight=0.058, width=80)
Registrar.configure(command=RegistrarB)
Registrar.configure(text="Registro")



Sair2 = Button(Registro)
Sair2.place(x=262, y=310, relheight=0.058, width=80)
Sair2.configure(command=Sair2)
Sair2.configure(text="Sair")

SenhaL = Label(Registro)
SenhaL.place(x=187, y=205, height=28, width=50)
SenhaL.configure(text="Senha")
SenhaL.configure(font="Arial")

TxtUsuario5 = Label(Registro)
TxtUsuario5.place(x=182, y=115, height=28, width=60)
TxtUsuario5.configure(text="Usuário")
TxtUsuario5.configure(font="Arial")
TxtUsuario5.configure(justify="center")
Registro.mainloop()


