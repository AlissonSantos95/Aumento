import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle
#import reportlab
import pdfkit
import tkinter as tk
import webbrowser
from tkinter import PhotoImage
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk
from time import time 
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Login = tk.ThemedTk()
Login.get_themes()
Login.set_theme("plastik")


#filename = PhotoImage(file ="LoginUI.png")
#background_label = Label(Login, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

width_of_window = 412
height_of_windows= 460
LarguraMonitor = Login.winfo_screenwidth()
AlturaMonitor = Login.winfo_screenheight()
x_cordinate = (LarguraMonitor/2) - (width_of_window/2)
y_cordinate = (AlturaMonitor/2) - (height_of_windows/2)
Login.geometry("%dx%d+%d+%d" % (width_of_window, height_of_windows, x_cordinate, y_cordinate))
Login.title("Aumento Salarial")
Login.minsize(116, 1)
Login.maxsize(1920, 1080)
Login.resizable(0, 0)
Login.update_idletasks()
Login.overrideredirect(1)

w = Canvas(Login, bg="grey", width=290, height=320)
w.place(x=63, y=70)

#.create_line(0, 0, 200, 100)
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))



#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario = Entry(Login)
Usuario.place(x=110, y=150, height=28, width=205)
Usuario.configure(font="TkFixedFont")
Usuario.configure(justify="center")

Senha1 = Entry(Login)
Senha1.place(x=110, y=240, height=28, width=205)
Senha1.configure(font="TkFixedFont")
Senha1.configure(show="*")
Senha1.configure(justify="center")
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim dos Inputs----------------------------------------------------------------------#
#-----------------------------------------------Inicio das Definições---------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#






def LoginA():
     Usuario2 = Usuario.get()
     Senha2 = Senha1.get()
     Registro13 = pickle.load(open("dat1.dat", "rb"))
     Registro12 = pickle.load(open("dat2.dat", "rb"))
     if Usuario2 == Registro12 :
             if Senha2== Registro13:
              msg=tk.messagebox.showinfo("Login", "Sucesso!")
              if (msg):
                  Login.destroy()
     if Usuario2 != Registro13:
         msg=tk.messagebox.showinfo("Login", "Erro de senha/usuario")
     if Senha2 != Registro12:
         msg=tk.messagebox.showinfo("Login", "Erro de senha/usuario")


def Sair2():
    msg=messagebox.askyesno("Sair","Gostaria de sair?")
    if (msg):
          sys.exit()

def Registrar():
    msg=messagebox.askyesno("Registrar", "Criar novo usuario?")
    if (msg):
      os.system("Resgistro.py")
def GitHUB():
    msg=messagebox.askyesno("GitHub", "Abrir GITHUB?")
    if(msg):
     url= "https://github.com/AlissonSantos95/Aumento"
     webbrowser.open(url)
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------fim Definições-----------------------------------------------------------------------------------------------#
#-----------------------------------------------Inicio Botões------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------Imagem do botão login-------------------------------#
#LoginBTN2 = PhotoImage(file="LoginBN.png")
#LoginBTN = Label(image=LoginBTN2)
#-------------Fim Image do botão login-------------------------------#


LoginB = Button(Login)
LoginB.place(x=77, y=310, relheight=0.058, width=80)
LoginB.configure(command=LoginA)
#LoginB.configure(image=LoginBTN2)
LoginB.configure(text="Login")


#----------------Imagem do botão login-------------------------------#
#SairBTN2 = PhotoImage(file="SairBN.png")
#SairBTN = Label(image=SairBTN2)
#-------------Fim Image do botão login-------------------------------#

Sair = Button(Login)
Sair.place(x=262, y=310, relheight=0.058, width=80)
Sair.configure(command=Sair2)
#Sair.configure(image=SairBTN2)
Sair.configure(text="Sair")
#----------------Imagem do botão Registro-------------------------------#
#RegistroBTN2 = PhotoImage(file="RegistroBN.png")
#RegistroBTN = Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro = Button(Login)
Registro.place(x=170, y=310, relheight=0.058, width=80)
Registro.configure(command=Registrar)
#Registro.configure(image=RegistroBTN2)
Registro.configure(text="Registrar")

#---------------Imagem do botão GitHub--------------------------------#
#GitHUBBTN2 = PhotoImage(file="GitBN.png")
#GitHUBBTN = Label(image=GitHUBBTN2)
#-------------Fim Image do botão GitHub-------------------------------#

Github = Button(Login)
Github.place(x=195, y=350, height=34, width=30)
Github.configure(command=GitHUB)
#Github.configure(image=GitHUBBTN2)
Github.configure(text="GIT")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Inicio Labels-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

SenhaL = Label(Login)
SenhaL.place(x=187, y=205, height=28, width=50)
SenhaL.configure(text="Senha")
SenhaL.configure(font="Arial")

TxtUsuario5 = Label(Login)
TxtUsuario5.place(x=182, y=115, height=28, width=60)
TxtUsuario5.configure(text="Usuário")
TxtUsuario5.configure(font="Arial")
TxtUsuario5.configure(justify="center")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------fim Labels-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


# Se alt+f4 é apertado execute------------------------------------------------------------------------------------------------------------
Alt_f4 = False  # Is Alt-F4 pressed?

def TenteSair():
    global Alt_f4
    if Alt_f4:
        print("Impedido")
        Alt_f4 = False  #Reinicia a variavel.
    else:
        TenteSair()

def alt_f4(event):
    global Alt_f4
    Alt_f4 = True

def Fechar(*event):
    Login.destroy()

# Fim Se alt+f4 é apertado execute------------------------------------------------------------------------------------------------------------
Login.bind('<Alt-F4>', alt_f4)
Login.bind('<Escape>', Fechar)
Login.protocol("WM_DELETE_WINDOW",TenteSair)
Login.mainloop()



#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim do codigo-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#