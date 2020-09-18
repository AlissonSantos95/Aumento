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

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Login = tk.Tk()


filename = PhotoImage(file ="LoginUI.png")
background_label = Label(Login, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


width_of_window = 450
height_of_windows= 350
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
Usuario.place(relx=0.330, rely=0.250,height=30, relwidth=0.350)
Usuario.configure(font="TkFixedFont")
Usuario.configure(highlightcolor="black")
Usuario.configure(borderwidth=0)
Usuario.configure(justify="center")

Senha1 = tk.Entry(Login)
Senha1.place(relx=0.330, rely=0.480,height=30, relwidth=0.350)
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
          quit

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
LoginB.place(relx=0.280, rely=0.625, relheight=0.080, relwidth=0.200)
LoginB.configure(command=LoginA)
LoginB.configure(image=LoginBTN2)
LoginB.configure(borderwidth=0)

#----------------Imagem do botão login-------------------------------#
SairBTN2 = PhotoImage(file="SairBN.png")
SairBTN = tk.Label(image=SairBTN2)
#-------------Fim Image do botão login-------------------------------#

Sair = tk.Button(Login)
Sair.place(relx=0.540, rely=0.625, relheight=0.0800, relwidth=0.200)
Sair.configure(command=Sair2)
Sair.configure(image=SairBTN2)
Sair.configure(borderwidth=0)

#----------------Imagem do botão Registro-------------------------------#
RegistroBTN2 = PhotoImage(file="RegistroBN.png")
RegistroBTN = tk.Label(image=RegistroBTN2)
#-------------Fim Image do botão Registro-------------------------------#

Registro = tk.Button(Login)
Registro.place(relx=0.405, rely=0.725, relheight=0.0800, relwidth=0.200)
Registro.configure(command=Registrar)
Registro.configure(image=RegistroBTN2)
Registro.configure(borderwidth=0)

#---------------Imagem do botão GitHub--------------------------------#
GitHUBBTN2 = PhotoImage(file="GitBN.png")
GitHUBBTN = tk.Label(image=GitHUBBTN2)
#-------------Fim Image do botão GitHub-------------------------------#

Github = tk.Button(Login)
Github.place(relx=0.405, rely=0.8900, relheight=0.0800, relwidth=0.200)
Github.configure(command=GitHUB)
Github.configure(image=GitHUBBTN2)
Github.configure(borderwidth=0)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim do codigo-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Login.mainloop()

