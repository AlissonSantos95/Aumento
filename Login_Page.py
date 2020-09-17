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
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


Login = tk.Tk()
Login.title("Aumento Salarial")
Login.geometry("450x350+509+249")
Login.minsize(116, 1)
Login.maxsize(1924, 1062)
Login.resizable(1, 1)



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
     if Usuario2 == "admin":
             if Senha2== "admin":
              msg=tk.messagebox.showinfo("Login", "Sucesso!")
              if (msg):
                  Login.destroy()
     if Usuario2 != "admin" and Senha2 != "admin":
         msg.tk.messagebox.showinfo("Login", "Erro de senha/usuario")
     
    #else:
      #msg=tk.messagebox.showinfo("Login", "Erro de senha/usuario")

def Sair():
    msg:tk.messagebox.askyesno("Sair","Gostaria de sair?")
    if (msg):
          exit()
def Registrar():
    msg:tk.messagebox.askyesno("Registrar", "Criar novo usuario?")
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
LoginB = tk.Button(Login)
LoginB.place(relx=0.340, rely=0.725, relheight=0.050, relwidth=0.125)
LoginB.configure(activebackground="#ececec")
LoginB.configure(activeforeground="#000000")
LoginB.configure(background="#d9d9d9")
LoginB.configure(disabledforeground="#a3a3a3")
LoginB.configure(foreground="#000000")
LoginB.configure(highlightbackground="#d9d9d9")
LoginB.configure(highlightcolor="black")
LoginB.configure(justify='left')
LoginB.configure(text='''Login''')
LoginB.configure(command=LoginA)

Sair = tk.Button(Login)
Sair.place(relx=0.540, rely=0.725, relheight=0.050, relwidth=0.125)
Sair.configure(activebackground="#ececec")
Sair.configure(activeforeground="#000000")
Sair.configure(background="#d9d9d9")
Sair.configure(disabledforeground="#a3a3a3")
Sair.configure(foreground="#000000")
Sair.configure(highlightbackground="#d9d9d9")
Sair.configure(highlightcolor="black")
Sair.configure(justify='left')
Sair.configure(text='''Sair''')
Sair.configure(command=Sair)

Registro = tk.Button(Login)
Registro.place(relx=0.540, rely=0.825, relheight=0.050, relwidth=0.125)
Registro.configure(activebackground="#ececec")
Registro.configure(activeforeground="#000000")
Registro.configure(background="#d9d9d9")
Registro.configure(disabledforeground="#a3a3a3")
Registro.configure(foreground="#000000")
Registro.configure(highlightbackground="#d9d9d9")
Registro.configure(highlightcolor="black")
Registro.configure(justify='left')
Registro.configure(text='''Registro''')
Registro.configure(command=Registrar)

Github = tk.Button(Login)
Github.place(relx=0.340, rely=0.825, relheight=0.050, relwidth=0.125)
Github.configure(activebackground="#ececec")
Github.configure(activeforeground="#000000")
Github.configure(background="#d9d9d9")
Github.configure(disabledforeground="#a3a3a3")
Github.configure(foreground="#000000")
Github.configure(highlightbackground="#d9d9d9")
Github.configure(highlightcolor="black")
Github.configure(justify='left')
Github.configure(text='''GitHub''')
Github.configure(command=GitHUB)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim do codigo-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Login.mainloop()

