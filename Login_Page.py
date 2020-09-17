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
Login = tk.Tk()

width_of_window = 450
height_of_windows= 350
LarguraMonitor = GetSystemMetrics(0)
AlturaMonitor = GetSystemMetrics(1)
x_cordinate = (LarguraMonitor/2) - (width_of_window/2)
y_cordinate = (AlturaMonitor/2) - (height_of_windows/2)
Login.geometry("%dx%d+%d+%d" % (width_of_window, height_of_windows, x_cordinate, y_cordinate))
Login.title("Aumento Salarial")
Login.minsize(116, 1)
Login.maxsize(1920, 1080)
Login.resizable(1, 1)
Login.update_idletasks()
Login.overrideredirect(1)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições da janela principal--------------------------------------------------#
#-----------------------------------------------Inicio Inputs.----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Usuario = tk.Entry(Login)
Usuario.place(relx=0.295, rely=0.325,height=30, relwidth=0.400)
Usuario.configure(background="white")
Usuario.configure(disabledforeground="#a3a3a3")
Usuario.configure(font="TkFixedFont")
Usuario.configure(foreground="#000000")
Usuario.configure(highlightbackground="#d9d9d9")
Usuario.configure(highlightcolor="black")
Usuario.configure(insertbackground="black")
Usuario.configure(selectbackground="blue")
Usuario.configure(selectforeground="white")

Senha1 = tk.Entry(Login)
Senha1.place(relx=0.295, rely=0.525,height=30, relwidth=0.400)
Senha1.configure(background="white")
Senha1.configure(disabledforeground="#a3a3a3")
Senha1.configure(font="TkFixedFont")
Senha1.configure(foreground="#000000")
Senha1.configure(highlightbackground="#d9d9d9")
Senha1.configure(highlightcolor="black")
Senha1.configure(insertbackground="black")
Senha1.configure(selectbackground="blue")
Senha1.configure(selectforeground="white")
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
LoginB.place(relx=0.340, rely=0.725, relheight=0.050, relwidth=0.125)
LoginB.configure(activebackground="#ececec")
LoginB.configure(activeforeground="#000000")
LoginB.configure(disabledforeground="#a3a3a3")
LoginB.configure(foreground="#000000")
LoginB.configure(highlightbackground="#d9d9d9")
LoginB.configure(highlightcolor="black")
LoginB.configure(justify='left')
LoginB.configure(text='''Login''')
LoginB.configure(command=LoginA)
LoginB.configure(pady=20)
LoginB.configure(image=LoginBTN2)
LoginB.configure(borderwidth=0)

#----------------Imagem do botão login-------------------------------#
SairBTN2 = PhotoImage(file="SairBN.png")
SairBTN = tk.Label(image=SairBTN2)
#-------------Fim Image do botão login-------------------------------#

Sair = tk.Button(Login)
Sair.place(relx=0.540, rely=0.725, relheight=0.050, relwidth=0.125)
Sair.configure(activebackground="#ececec")
Sair.configure(activeforeground="#000000")
Sair.configure(disabledforeground="#a3a3a3")
Sair.configure(foreground="#000000")
Sair.configure(highlightbackground="#d9d9d9")
Sair.configure(highlightcolor="black")
Sair.configure(justify='left')
Sair.configure(text='''Sair''')
Sair.configure(command=Sair)
Sair.configure(pady=20)
Sair.configure(command=Sair2)
Sair.configure(image=SairBTN2)
Sair.configure(borderwidth=0)

#----------------Imagem do botão Registro-------------------------------#
RegistroBTN2 = PhotoImage(file="RegistroBN.png")
RegistroBTN = tk.Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro = tk.Button(Login)
Registro.place(relx=0.540, rely=0.825, relheight=0.050, relwidth=0.125)
Registro.configure(activebackground="#ececec")
Registro.configure(activeforeground="#000000")
Registro.configure(disabledforeground="#a3a3a3")
Registro.configure(foreground="#000000")
Registro.configure(highlightbackground="#d9d9d9")
Registro.configure(highlightcolor="black")
Registro.configure(justify='left')
Registro.configure(text='''Registro''')
Registro.configure(command=Registrar)
Registro.configure(pady=20)
Registro.configure(image=RegistroBTN2)
Registro.configure(borderwidth=0)

#---------------Imagem do botão GitHub--------------------------------#
GitHUBBTN2 = PhotoImage(file="GitBN.png")
GitHUBBTN = tk.Label(image=GitHUBBTN2)
#-------------Fim Image do botão GitHub-------------------------------#

Github = tk.Button(Login)
Github.place(relx=0.340, rely=0.825, relheight=0.050, relwidth=0.125)
Github.configure(activebackground="#ececec")
Github.configure(activeforeground="#000000")
Github.configure(disabledforeground="#a3a3a3")
Github.configure(foreground="#000000")
Github.configure(highlightbackground="#d9d9d9")
Github.configure(highlightcolor="black")
Github.configure(justify='left')
Github.configure(text='''GitHub''')
Github.configure(command=GitHUB)
Github.configure(pady=20)
Github.configure(image=GitHUBBTN2)
Github.configure(borderwidth=0)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim do codigo-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Login.mainloop()

