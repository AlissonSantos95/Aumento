import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle

import pdfkit
import tkinter as tk
from tkinter import * 
from Login_Page import Login
from tkinter import PhotoImage
from tkinter.ttk import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

##-----------------------------------------------------------------------------------------------------------------------------------#
##-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
##-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
##-----------------------------------------------------------------------------------------------------------------------------------##
Aumento = tk.ThemedTk()
Aumento.get_themes()
Aumento.set_theme("plastik")

width_of_window = 790
height_of_windows= 350
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
        msg=messagebox.askyesno("PDF", "Salvar Formação Fundamental?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("fundamental1.txt", "1PDFFundamental.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("fundamental2.txt", "2PDFFundamental2.pdf",configuration=config)
        msg=messagebox.askyesno("PDF", "Salvar Formação Medio?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Medio1.txt", "1PDFMedio.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Medio2.txt", "2PDFMedio.pdf",configuration=config)
        msg=messagebox.askyesno("PDF", "Salvar Formação Tecnico?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Tecnico1.txt", "1PDFTecnico.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Tecnico2.txt", "2PDFTecnico.pdf",configuration=config)
        msg=messagebox.askyesno("PDF", "Salvar Formação Analfabeto?")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Analfabeto1.txt", "1PDFAnalfabeto.pdf",configuration=config)

            pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Analfabeto2.txt", "2PDFAnalfabeto.pdf",configuration=config)
        msg=messagebox.askyesno("PDF", "Salvar Formação Superior??")
        if (msg):
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Superior2.txt", "1PDFSuperior.pdf",configuration=config)

            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file("Superior2.txt", "2PDFSuperior.pdf",configuration=config)
        msg=messagebox.askyesno("PDF", "Salvar Formação Doutorado?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                  msg1=messagebox.showinfo("Aumento de", results)
                  msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
                 msg1=messagebox.showinfo("Aumento de", results)
                 msg=messagebox.askyesno("salvar", "Deseja salvar?")
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
def Demitir():
         Soldo1 = Salario2.get()
         Dias = Diasde.get()
         Mes1 = MesT.get()
         filhos2 = filhos.get()
         nomes =Nome1.get()
         funcionarios = funcionario.get()
         fgts1 = float(Soldo1) * (8/100)
         fgts2 = float(fgts1) * float(Mes1)
         FeriasP= float(Soldo1) * float(Mes1)
         FeriasPT=float(FeriasP) / 12
         FeriasPT2=float(FeriasPT) / 3

         filhost = int(filhos2) * 48.62
         ValorMes = float(Soldo1) / 12
         ValorDia = float(ValorMes) /30
         ValorDIAS = float(ValorDia) * float(Dias)
         ValorMeses= float(ValorMes) * int(Mes1)
         if float(Soldo1) <= float(1046):
                C13 = float(Soldo1) * (7.5/100)
         else:
             if float(Soldo1) >= 1046 and float(Soldo1) < 2090:
                  C13 = float(Soldo1) * (9/100)
         if float(Soldo1) >= 2090 and float(Soldo1) < 3135:
             C13 = float(Soldo1) * (12/100)
         else:
             if float(Soldo1) >3135:
               C13= float(Soldo1) * (14/100)

         C13R = float(C13) * float(Mes1)


         results2= "Salario: ",Soldo1,"      ", "MultaFGTS(sem os dias): " ,fgts2,"      ", "Ferias Proporcional: ", FeriasPT,"     ", "1/3 Ferias: ",FeriasPT2,"         ","13º: ",ValorMeses, "         ","INSS POR MES: ",C13, "         ","INSS Total(Sem 13): ",C13R
         msg=messagebox.showinfo("resultados", results2)


def Pdemitir():
         Soldo1 = Salario2.get()
         Dias = Diasde.get()
         Mes1 = MesT.get()
         filhos2 = filhos.get()
         nomes =Nome1.get()
         funcionarios = funcionario.get()
         FeriasP= float(Soldo1) * float(Mes1)
         FeriasPT=float(FeriasP) / 12
         FeriasPT2=float(FeriasPT) / 3
         filhost = int(filhos2) * 48.62
         ValorMes = float(Soldo1) / 12
         ValorDia = float(ValorMes) /30
         ValorDIAS = float(ValorDia) * float(Dias)
         ValorMeses= float(ValorMes) * int(Mes1)
         if float(Soldo1) <= float(1046):
                C13 = float(Soldo1) * (7.5/100)
         else:
             if float(Soldo1) >= 1046 and float(Soldo1) < 2090:
                  C13 = float(Soldo1) * (9/100)
         if float(Soldo1) >= 2090 and float(Soldo1) < 3135:
             C13 = float(Soldo1) * (12/100)
         else:
             if float(Soldo1) >3135:
               C13= float(Soldo1) * (14/100)

         C13R = float(C13) * float(Mes1)


         results2= "Salario: ",Soldo1,"      ", "Ferias Proporcional: ", FeriasPT,"     ", "1/3 Ferias: ",FeriasPT2,"         ","13º: ",ValorMeses, "         ","INSS POR MES: ",C13, "         ","INSS Total(Sem 13): ",C13R
         msg=messagebox.showinfo("resultados", results2)

def justac():
         Soldo1 = float(Salario2.get())
         Dias = Diasde.get()
         Mes1 = MesT.get()
         filhos2 = filhos.get()
         nomes =Nome1.get()
         funcionarios = funcionario.get()
         FeriasP= float(Soldo1) * float(Mes1)
         FeriasPT=float(FeriasP) / 12
         FeriasPT2=float(FeriasPT) / 3

         if float(Soldo1) <= float(1046):
                C13 = float(Soldo1) * (7.5/100)
         else:
             if float(Soldo1) >= 1046 and float(Soldo1) < 2090:
                  C13 = float(Soldo1) * (9/100)
         if float(Soldo1) >= 2090 and float(Soldo1) < 3135:
             C13 = float(Soldo1) * (12/100)
         else:
             if float(Soldo1) >3135:
               C13= float(Soldo1) * (14/100)

         C13R = float(C13) * float(Mes1)
         results2= "Salario: ",Soldo1,"      ","      ", "Ferias Proporcional: ", FeriasPT,"     ", "1/3 Ferias: ",FeriasPT2,"         ","INSS POR MES: ",C13, "         ","INSS Total(Sem 13): ",C13R
         msg=messagebox.showinfo("resultados", results2)
def SairNew():
         msg=messagebox.askyesno("Sair", "Deseja Realmente Sair?")
         if(msg):
             sys.exit()
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições das variaveis dos Botões---------------------------------------------#
#-----------------------------------------------Inicio Botões-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
Analfabeto = Button(Aumento)
Analfabeto.place(x=10, y=210, height=32, width=100)
Analfabeto.configure(command=AnalfabetoE)
Analfabeto.configure(text="Analfabeto")

fundamental = Button(Aumento)
fundamental.place(x=145, y=210, height=32, width=100)
fundamental.configure(command=FundamentalA)
fundamental.configure(text="Fundamental")

Medio = Button(Aumento)
Medio.place(x=275, y=210, height=32, width=100)
Medio.configure(command=MedioB)
Medio.configure(text="Medio")

Tecnico = Button(Aumento)
Tecnico.place(x=10, y=250, height=32, width=100)
Tecnico.configure(command=TecnicoC)
Tecnico.configure(text="Tecnico")

Superior = Button(Aumento)
Superior.place(x=145, y=250, height=32, width=100)
Superior.configure(command=SuperiorD)
Superior.configure(text="Superior")

Doutorado = Button(Aumento)
Doutorado.place(x=275, y=250, height=32, width=100)
Doutorado.configure(command=DoutoradoF)
Doutorado.configure(text="Doutorado")

PDF = Button(Aumento)
PDF.place(x=275, y=290, height=32, width=100)
PDF.configure(command=exportar)
PDF.configure(text="PDF")

DefinaV1= Button(Aumento)
DefinaV1.place(x=145, y=290, height=32, width=100)
DefinaV1.configure(text="Definir")

Sair3 = Button(Aumento)
Sair3.place(x=10, y=290, height=32, width=100)
Sair3.configure(command=SairNew)
Sair3.configure(text="Sair")

DemitirB = Button(Aumento)
DemitirB.place(x=665, y=250, height=32, width=100)
DemitirB.configure(command=Demitir)
DemitirB.configure(text="Demissão")

Pdemissao = Button(Aumento)
Pdemissao.place(x=545, y=250, height=32, width=100)
Pdemissao.configure(command=Pdemitir)
Pdemissao.configure(text="Pedido Dem.")

JustaCB = Button(Aumento)
JustaCB.place(x=430, y=250, height=32, width=100)
JustaCB.configure(command=justac)
JustaCB.configure(text="Justa Causa")


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio entrada de inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

funcionario = Entry(Aumento)
funcionario.place(x=200, y=5,height=25, width=189)
funcionario.configure(font="TkFixedFont")
funcionario.configure(justify="center")

Nome1 = Entry(Aumento)
Nome1.place(x=200, y=45, height=25, width=189)
Nome1.configure(font="TkFixedFont")
Nome1.configure(justify="center")

Idade = Entry(Aumento)
Idade.place(x=200, y=85,height=25, width=189)
Idade.configure(font="TkFixedFont")
Idade.configure(justify="center")

Salario = Entry(Aumento)
Salario.place(x=200, y=125 ,height=25, width=189)
Salario.configure(font="TkFixedFont")
Salario.configure(justify="center")

Exp= Entry(Aumento)
Exp.place(x=200, y=165,height=25, width=189)
Exp.configure(font="TkFixedFont")
Exp.configure(justify="center")
#------------------------------------Entrada de demissão---------------------------------
Salario2 = Entry(Aumento)
Salario2.place(x=590, y=5,height=25, width=189)
Salario2.configure(font="TkFixedFont")
Salario2.configure(justify="center")


MesT = Entry(Aumento)
MesT.place(x=590, y=45, height=25, width=189)
MesT.configure(font="TkFixedFont")
MesT.configure(justify="center")

Diasde = Entry(Aumento)
Diasde.place(x=590, y=85,height=25, width=189)
Diasde.configure(font="TkFixedFont")
Diasde.configure(justify="center")

filhos = Entry(Aumento)
filhos.place(x=590,  y=125 ,height=25, width=189)
filhos.configure(font="TkFixedFont")
filhos.configure(justify="center")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio Labels para inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

NumeroF = Label(Aumento)
NumeroF.place(x=0, y=2, height=28, width=170)
NumeroF.configure(text="Numero do Funcionário:")
NumeroF.configure(font="Arial")

Nomef = Label(Aumento)
Nomef.place(x=0, y=43, height=28, width=170)
Nomef.configure(text="Nome do Funcionário:")
Nomef.configure(font="Arial")

IdadeF = Label(Aumento)
IdadeF.place(x=0, y=83, height=28, width=170)
IdadeF.configure(text="Idade do funcionário:")
IdadeF.configure(font="Arial")

SoldoF = Label(Aumento)
SoldoF.place(x=0, y=123, height=28, width=170)
SoldoF.configure(text="Salário do funcionário:")
SoldoF.configure(font="Arial")

ExpF = Label(Aumento)
ExpF.place(x=0, y=163, height=28, width=189)
ExpF.configure(text="Experiencia do funcionário:")
ExpF.configure(font="Arial")

Salario22 = Label(Aumento)
Salario22.place(x=410, y=2, height=28, width=170)
Salario22.configure(text="Salário:")
Salario22.configure(font="Arial")

MesTrabalhado = Label(Aumento)
MesTrabalhado.place(x=410, y=43, height=28, width=170)
MesTrabalhado.configure(text="Meses Trabalhado")
MesTrabalhado.configure(font="Arial")

DiasTrabalhado = Label(Aumento)
DiasTrabalhado.place(x=410, y=83, height=28, width=170)
DiasTrabalhado.configure(text="Dias Trabalhado")
DiasTrabalhado.configure(font="Arial")

Filhos1 = Label(Aumento)
Filhos1.place(x=410, y=123, height=28, width=170)
Filhos1.configure(text="Tem Filhos?")
Filhos1.configure(font="Arial")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim labels para inputs--------------------------------------------------------------#
#-----------------------------------------------Inicio Separadores------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

TSeparator1 = Separator(Aumento)
TSeparator1.place(x=400, y=0, height=900)
TSeparator1.configure(orient="vertical")


#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim separadores---------------------------------------------------------------------#
#-----------------------------------------------Inicio Caixa de texto-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Aumento.mainloop()
Login.mainloop()
