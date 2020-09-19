import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle
import reportlab
import pdfkit
import tkinter as tk
from tkinter import * 
from Login_Page import Login
from tkinter import PhotoImage
from tkinter.ttk import *


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


Aumento = tk.Tk()


filename = PhotoImage(file ="NewOneUI.png")
background_label = Label(Aumento, image=filename)
background_label.place(x=0, y=0)



width_of_window = 1035
height_of_windows= 730
LarguraMonitor = Aumento.winfo_screenwidth()
AlturaMonitor = Aumento.winfo_screenheight()
x_cordinate = (LarguraMonitor/2) - (width_of_window/2)
y_cordinate = (AlturaMonitor/2) - (height_of_windows/2)
Aumento.geometry("%dx%d+%d+%d" % (width_of_window, height_of_windows, x_cordinate, y_cordinate))
Aumento.title("Aumento Salarial")
Aumento.minsize(116, 1)
Aumento.maxsize(1920, 1080)
Aumento.resizable(0, 0)
Aumento.update_idletasks()
Aumento.overrideredirect(0)

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim configuração Aumento(janela inicial)--------------------------------------------#
#-----------------------------------------------Inicio Definições de botão clicado--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

def exportar() :
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Fundamental?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("fundamental1.txt", "1PDFFundamental.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("fundamental2.txt", "2PDFFundamental2.pdf",configuration=config)
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Medio?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Medio1.txt", "1PDFMedio.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Medio2.txt", "2PDFMedio.pdf",configuration=config)
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Tecnico?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Tecnico1.txt", "1PDFTecnico.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Tecnico2.txt", "2PDFTecnico.pdf",configuration=config)
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Analfabeto?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Analfabeto1.txt", "1PDFAnalfabeto.pdf",configuration=config)

            pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Analfabeto2.txt", "2PDFAnalfabeto.pdf",configuration=config)
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Superior??")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Superior2.txt", "1PDFSuperior.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Superior2.txt", "2PDFSuperior.pdf",configuration=config)
        msg=tk.messagebox.askyesno("PDF", "Salvar Formação Doutorado?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Doutorado1.txt", "1PDFDoutorado.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Doutorado1.txt", "2PDFDoutorado.pdf",configuration=config)
def FundamentalA():
         Formacao = "F"
         import pickle
         nomes = Nome1.get()
         idades = Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         if Formacao == "F" :
             if int(idades) >= 18 or int(exp) >= 3:
                 aumento = float(Soldo) * 0.10
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("fundamental1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 18 and int(exp) < 3:
                 aumento = float(Soldo) * 0.05
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("fundamental2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
def MedioB():
         Formacao = "M"
         nomes =Nome1.get()
         idades = Idade.get()
         exp =Exp.get()
         Soldo =Salario.get()
         funcionarios =funcionario.get()
         if Formacao == "M" :
             if int(idades) >= 20 or int(exp) >= 5:
                 aumento = float(Soldo) * 0.20
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("Medio1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 20 and int(exp) < 5:
                 aumento = float(Soldo) * 0.10
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("Medio2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
def TecnicoC():
         Formacao = "T"
         nomes = Nome1.get()
         idades = Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         if Formacao == "T" :
             if int(idades) >= 25 or int(exp) >= 7:
                 aumento = float(Soldo) * 0.30
                 aumento1 = aumento
                 results = "seu aumento foi de", aumento1
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Tecnico1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 25 and int(exp) < 7:
                 aumento = float(Soldo) * 0.20
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Tecnico1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
def AnalfabetoE():
         Formacao = "A"
         nomes = Nome1.get()
         idades =Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         if Formacao == "A" :
             if int(idades) >= 40 or int(exp) >= 12:
                  aumento = float(Soldo) * 0.50
                  results = "seu aumento foi de", aumento
                  msg1=tk.messagebox.showinfo("Aumento de", results)
                  msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                  if (msg):
                     with open("Analfabeto1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 18 or int(exp) >=4:
                 aumento = float(Soldo) * 0.40
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Analfabeto2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
def SuperiorD():
         
         Formacao = "S"
         nomes = Nome1.get()
         idades = Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         if Formacao == "S" :
             if int(idades) >= 30 or int(exp) >= 10:
                 aumento = float(Soldo) * 0.40
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Superior1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 18 and int(exp) < 10:
                 aumento = float(Soldo) * 0.30
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")


def DoutoradoF():
         Formacao = "D"
         nomes =Nome1.get()
         idades = Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         #dissidio = DissidioA.get()
         if Formacao == "D" :
             if int(idades) >= 45 or int(exp) >= 20:
                 aumento = float(Soldo) * 0.80
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Doutorado1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
             if int(idades) < 18 and int(exp) < 3:
                 aumento = float(Soldo) * 0.05
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("doutorado2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------\n")
                          f.write("Funcionario:" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          #f.write("Aumento de:" + aumento + "\n")
                          f.write("Salario:" + Soldo +"\n")
                          f.write("-------------------------------------------------------------------------------------------\n")
def SairNew():
         msg=tk.messagebox.askyesno("Sair", "Deseja Realmente Sair?")
         if(msg):
             exit()
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições das variaveis dos Botões---------------------------------------------#
#-----------------------------------------------Inicio Botões-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


#----------------Imagem do botão Fundamental-------------------------------#
fundamentalBTN2 = PhotoImage(file="fundamentalBN.png")
fundamentalLBTN = tk.Label(image=fundamentalBTN2)
#-------------Fim Image do botão Fundamental-------------------------------#

fundamental = tk.Button(Aumento)
fundamental.place(relx=0.650, rely=0.20, height=32, relwidth=0.125)
fundamental.configure(command=FundamentalA)
fundamental.configure(image=fundamentalBTN2)
fundamental.configure(borderwidth=1)

#----------------Imagem do botão Medio-------------------------------#
MedioBTN2 = PhotoImage(file="MedioBN.png")
MedioBTN = tk.Label(image=MedioBTN2)
#-------------Fim Image do botão Medio-------------------------------#

Medio = tk.Button(Aumento)
Medio.place(relx=0.840, rely=0.20, height=32, relwidth=0.125)
Medio.configure(command=MedioB)
Medio.configure(image=MedioBTN2)
Medio.configure(borderwidth=1)

#----------------Imagem do botão Tecnico-------------------------------#
TecnicoBTN2 = PhotoImage(file="TecnicoBN.png")
TecnicoBTN = tk.Label(image=TecnicoBTN2)
#-------------Fim Image do botão login-------------------------------#

Tecnico = tk.Button(Aumento)
Tecnico.place(relx=0.478, rely=0.28, height=32, relwidth=0.125)
Tecnico.configure(command=TecnicoC)
Tecnico.configure(image=TecnicoBTN2)
Tecnico.configure(borderwidth=1)

#----------------Imagem do botão login-------------------------------#
AnalfabetoBTN2 = PhotoImage(file="AnalfabetoBN.png")
analfabetoBTN = tk.Label(image=AnalfabetoBTN2)
#-------------Fim Image do botão login-------------------------------#

Analfabeto = tk.Button(Aumento)
Analfabeto.place(relx=0.478, rely=0.20, height=32, relwidth=0.125)
Analfabeto.configure(command=AnalfabetoE)
Analfabeto.configure(image=AnalfabetoBTN2)
Analfabeto.configure(borderwidth=1)

#----------------Imagem do botão login-------------------------------#
SuperiorBTN2 = PhotoImage(file="SuperiorBN.png")
SuperiorBTN = tk.Label(image=SuperiorBTN2)
#-------------Fim Image do botão login-------------------------------#

Superior = tk.Button(Aumento)
Superior.place(relx=0.650, rely=0.28, height=32, relwidth=0.125)
Superior.configure(command=SuperiorD)
Superior.configure(borderwidth=1)
Superior.configure(image=SuperiorBTN2)

#----------------Imagem do botão login-------------------------------#
PDFBTN2 = PhotoImage(file="PDFBN.png")
PDFBTN = tk.Label(image=PDFBTN2)
#-------------Fim Image do botão login-------------------------------#

PDF = tk.Button(Aumento)
PDF.place(relx=0.150112, rely=0.915, height=32, relwidth=0.125)
PDF.configure(command=exportar)
PDF.configure(image=PDFBTN2)
PDF.configure(borderwidth=1)

#----------------Imagem do botão login-------------------------------#
DoutorBTN2 = PhotoImage(file="DoutorBN.png")
DoutorBTN = tk.Label(image=DoutorBTN2)
#-------------Fim Image do botão login-------------------------------#

Doutorado = tk.Button(Aumento)
Doutorado.place(relx=0.840, rely=0.28, height=32, relwidth=0.125)
Doutorado.configure(command=DoutoradoF)
Doutorado.configure(image=DoutorBTN2)
Doutorado.configure(borderwidth=1)

#----------------Imagem do botão login-------------------------------#
SairBTN3 = PhotoImage(file="SairBN.png")
SairBTN = tk.Label(image=SairBTN3)
#-------------Fim Image do botão login-------------------------------#

Sair3 = tk.Button(Aumento)
Sair3.place(relx=0.650, rely=0.04, height=32, relwidth=0.125)
Sair3.configure(command=SairNew)
Sair3.configure(image=SairBTN3)
Sair3.configure(borderwidth=1)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio entrada de inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

funcionario = tk.Entry(Aumento)
funcionario.place(relx=0.219, rely=0.20,height=25, relwidth=0.182)
funcionario.configure(font="TkFixedFont")
funcionario.configure(highlightcolor="black")
funcionario.configure(borderwidth=2)
funcionario.configure(justify="center")

Nome1 = tk.Entry(Aumento)
Nome1.place(relx=0.219, rely=0.27,height=25, relwidth=0.182)
Nome1.configure(font="TkFixedFont")
Nome1.configure(highlightcolor="black")
Nome1.configure(borderwidth=2)
Nome1.configure(justify="center")

Idade = tk.Entry(Aumento)
Idade.place(relx=0.219, rely=0.33,height=25, relwidth=0.182)
Idade.configure(font="TkFixedFont")
Idade.configure(highlightcolor="black")
Idade.configure(borderwidth=2)
Idade.configure(justify="center")

Salario = tk.Entry(Aumento)
Salario.place(relx=0.219, rely=0.39,height=25, relwidth=0.182)
Salario.configure(font="TkFixedFont")
Salario.configure(highlightcolor="black")
Salario.configure(borderwidth=2)
Salario.configure(justify="center")

Exp = tk.Entry(Aumento)
Exp.place(relx=0.219, rely=0.45,height=25, relwidth=0.182)
Exp.configure(font="TkFixedFont")
Exp.configure(highlightcolor="black")
Exp.configure(borderwidth=2)
Exp.configure(justify="center")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio Labels para inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

#Labels foram removidas devido ao uso de imagem na parte design

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim labels para inputs--------------------------------------------------------------#
#-----------------------------------------------Inicio Separadores------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

#Separadores foram removidas devido ao uso de imagem na parte design

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim separadores---------------------------------------------------------------------#
#-----------------------------------------------Inicio Caixa de texto-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Aumento.mainloop()
Login.mainloop()