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
from PIL import Image, ImageTk
from time import time 
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Login = tk.Tk()


filename = PhotoImage(file ="LoginUI.png")
background_label = Label(Login, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


width_of_window = 812
height_of_windows= 612
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


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario = tk.Entry(Login)
Usuario.place(relx=0.358, rely=0.533,height=28, relwidth=0.305)
Usuario.configure(font="TkFixedFont")
Usuario.configure(highlightcolor="black")
Usuario.configure(borderwidth=0)
Usuario.configure(justify="center")

Senha1 = tk.Entry(Login)
Senha1.place(relx=0.358, rely=0.679,height=28, relwidth=0.305)
Senha1.configure(font="TkFixedFont")
Senha1.configure(highlightcolor="black")
Senha1.configure(borderwidth=0)
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
    msg=tk.messagebox.askyesno("Sair","Gostaria de sair?")
    if (msg):
          exit()

def Registrar():
    msg=tk.messagebox.askyesno("Registrar", "Criar novo usuario?")
    if (msg):
      os.system("registro.py")
def GitHUB():
    msg=tk.messagebox.askyesno("GitHub", "Abrir GITHUB?")
    if(msg):
     url= "https://github.com/AlissonSantos95/Aumento"
     webbrowser.open(url)
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------fim Definições-----------------------------------------------------------------------------------------------#
#-----------------------------------------------Inicio Botões------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------Imagem do botão login-------------------------------#
LoginBTN2 = PhotoImage(file="LoginBN.png")
LoginBTN = tk.Label(image=LoginBTN2)
#-------------Fim Image do botão login-------------------------------#


LoginB = tk.Button(Login)
LoginB.place(relx=0.335, rely=0.760, relheight=0.058, relwidth=0.145)
LoginB.configure(command=LoginA)
LoginB.configure(image=LoginBTN2)
LoginB.configure(borderwidth=1)


#----------------Imagem do botão login-------------------------------#
SairBTN2 = PhotoImage(file="SairBN.png")
SairBTN = tk.Label(image=SairBTN2)
#-------------Fim Image do botão login-------------------------------#

Sair = tk.Button(Login)
Sair.place(relx=0.533, rely=0.760, relheight=0.058, relwidth=0.145)
Sair.configure(command=Sair2)
Sair.configure(image=SairBTN2)
Sair.configure(borderwidth=1)

#----------------Imagem do botão Registro-------------------------------#
RegistroBTN2 = PhotoImage(file="RegistroBN.png")
RegistroBTN = tk.Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro = tk.Button(Login)
Registro.place(relx=0.429, rely=0.827, relheight=0.058, relwidth=0.145)
Registro.configure(command=Registrar)
Registro.configure(image=RegistroBTN2)
Registro.configure(borderwidth=1)

#---------------Imagem do botão GitHub--------------------------------#
GitHUBBTN2 = PhotoImage(file="GitBN.png")
GitHUBBTN = tk.Label(image=GitHUBBTN2)
#-------------Fim Image do botão GitHub-------------------------------#

Github = tk.Button(Login)
Github.place(relx=0.485, rely=0.919, relheight=0.059, relwidth=0.042)
Github.configure(command=GitHUB)
Github.configure(image=GitHUBBTN2)
Github.configure(borderwidth=1)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim do codigo-----------------------------------------------------------------------#
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



