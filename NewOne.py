import sys
import os
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pickle
import reportlab
import pdfkit
import tkinter as tk
from Login_Page import Login



#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Importação de modulos-----------------------------------------------------------#
#-----------------------------------------------Inicio criação da janela principal--------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#


Aumento = tk.Tk()
Aumento.title("Aumento Salarial")
Aumento.geometry("739x499+509+249")
Aumento.minsize(116, 1)
Aumento.maxsize(1924, 1062)
Aumento.resizable(1, 1)

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
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 18 and int(exp) < 3:
                 aumento = float(Soldo) * 0.05
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("fundamental2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
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
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 20 and int(exp) < 5:
                 aumento = float(Soldo) * 0.10
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("Medio2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
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
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                      with open("Tecnico1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 25 and int(exp) < 7:
                 aumento = float(Soldo) * 0.20
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Tecnico2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
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
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 12 and int(exp) < 12:
                 aumento = float(Soldo) * 0.40
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Analfabeto2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
def SuperiorD():
         print("teste")
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
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 18 and int(exp) < 10:
                 aumento = float(Soldo) * 0.30
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Superior2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
def DoutoradoF():
         Formacao = "D"
         nomes =Nome1.get()
         idades = Idade.get()
         exp = Exp.get()
         Soldo = Salario.get()
         funcionarios = funcionario.get()
         if Formacao == "D" :
             if int(idades) >= 45 or int(exp) >= 20:
                 aumento = float(Soldo) * 0.80
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("Doutorado1.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")
             if int(idades) < 18 and int(exp) < 3:
                 aumento = float(Soldo) * 0.05
                 results = "seu aumento foi de", aumento
                 msg1=tk.messagebox.showinfo("Aumento de", results)
                 msg=tk.messagebox.askyesno("salvar", "Deseja salvar?")
                 if (msg):
                     with open("doutorado2.txt", "a") as f:
                          f.write("-----------------------------------------------------------------------------------------" + "\n")
                          f.Write("Funcionario" + funcionarios + "\n")
                          f.write("Nome:" + nomes + "\n" )
                          f.write("Idade:" + idades + "\n")
                          f.write("Experiencia:" +exp + "\n")
                          f.write("Salario:" + Soldo + "\n")
                          f.write("-------------------------------------------------------------------------------------------" + "\n")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim definições das variaveis dos Botões---------------------------------------------#
#-----------------------------------------------Inicio Botões-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

fundamental = tk.Button(Aumento)
fundamental.place(relx=0.014, rely=0.541, relheight=0.050, relwidth=0.050)
fundamental.configure(activebackground="#ececec")
fundamental.configure(activeforeground="#000000")
fundamental.configure(background="#d9d9d9")
fundamental.configure(disabledforeground="#a3a3a3")
fundamental.configure(foreground="#000000")
fundamental.configure(highlightbackground="#d9d9d9")
fundamental.configure(highlightcolor="black")
fundamental.configure(justify='left')
fundamental.configure(text='''F''')
fundamental.configure(command=FundamentalA)

Medio = tk.Button(Aumento)
Medio.place(relx=0.014, rely=0.600, relheight=0.050, relwidth=0.050)
Medio.configure(activebackground="#ececec")
Medio.configure(activeforeground="#000000")
Medio.configure(background="#d9d9d9")
Medio.configure(disabledforeground="#a3a3a3")
Medio.configure(foreground="#000000")
Medio.configure(highlightbackground="#d9d9d9")
Medio.configure(highlightcolor="black")
Medio.configure(justify='left')
Medio.configure(text='''M''')
Medio.configure(command=MedioB)

Tecnico = tk.Button(Aumento)
Tecnico.place(relx=0.122, rely=0.541, relheight=0.050, relwidth=0.050)
Tecnico.configure(activebackground="#ececec")
Tecnico.configure(activeforeground="#000000")
Tecnico.configure(background="#d9d9d9")
Tecnico.configure(disabledforeground="#a3a3a3")
Tecnico.configure(foreground="#000000")
Tecnico.configure(highlightbackground="#d9d9d9")
Tecnico.configure(highlightcolor="black")
Tecnico.configure(justify='left')
Tecnico.configure(text='''T''')
Tecnico.configure(command=TecnicoC)

Analfabeto = tk.Button(Aumento)
Analfabeto.place(relx=0.122, rely=0.600, relheight=0.050, relwidth=0.050)
Analfabeto.configure(activebackground="#ececec")
Analfabeto.configure(activeforeground="#000000")
Analfabeto.configure(background="#d9d9d9")
Analfabeto.configure(disabledforeground="#a3a3a3")
Analfabeto.configure(foreground="#000000")
Analfabeto.configure(highlightbackground="#d9d9d9")
Analfabeto.configure(highlightcolor="black")
Analfabeto.configure(justify='left')
Analfabeto.configure(text='''A''')
Analfabeto.configure(command=AnalfabetoE)

Superior = tk.Button(Aumento)
Superior.place(relx=0.222, rely=0.541, relheight=0.050, relwidth=0.050)
Superior.configure(activebackground="#ececec")
Superior.configure(activeforeground="#000000")
Superior.configure(background="#d9d9d9")
Superior.configure(disabledforeground="#a3a3a3")
Superior.configure(foreground="#000000")
Superior.configure(highlightbackground="#d9d9d9")
Superior.configure(highlightcolor="black")
Superior.configure(justify='left')
Superior.configure(text='''S''')
Superior.configure(command=SuperiorD)

PDF = tk.Button(Aumento)
PDF.place(relx=0.65, rely=0.02, height=34, width=87)
PDF.configure(activebackground="#ececec")
PDF.configure(activeforeground="#000000")
PDF.configure(background="#d9d9d9")
PDF.configure(disabledforeground="#a3a3a3")
PDF.configure(foreground="#000000")
PDF.configure(highlightbackground="#d9d9d9")
PDF.configure(highlightcolor="black")
PDF.configure(pady="0")
PDF.configure(text='''PDF''')
PDF.configure(command=exportar)

Doutorado = tk.Button(Aumento)
Doutorado.place(relx=0.222, rely=0.600, relheight=0.050, relwidth=0.050)
Doutorado.configure(activebackground="#ececec")
Doutorado.configure(activeforeground="#000000")
Doutorado.configure(background="#d9d9d9")
Doutorado.configure(disabledforeground="#a3a3a3")
Doutorado.configure(foreground="#000000")
Doutorado.configure(highlightbackground="#d9d9d9")
Doutorado.configure(highlightcolor="black")
Doutorado.configure(justify='left')
Doutorado.configure(text='''D''')
Doutorado.configure(command=DoutoradoF)
#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio entrada de inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

funcionario = tk.Entry(Aumento)
funcionario.place(relx=0.257, rely=0.02,height=20, relwidth=0.154)
funcionario.configure(background="white")
funcionario.configure(disabledforeground="#a3a3a3")
funcionario.configure(font="TkFixedFont")
funcionario.configure(foreground="#000000")
funcionario.configure(highlightbackground="#d9d9d9")
funcionario.configure(highlightcolor="black")
funcionario.configure(insertbackground="black")
funcionario.configure(selectbackground="blue")
funcionario.configure(selectforeground="white")

Nome1 = tk.Entry(Aumento)
Nome1.place(relx=0.257, rely=0.12,height=20, relwidth=0.154)
Nome1.configure(background="white")
Nome1.configure(disabledforeground="#a3a3a3")
Nome1.configure(font="TkFixedFont")
Nome1.configure(foreground="#000000")
Nome1.configure(highlightbackground="#d9d9d9")
Nome1.configure(highlightcolor="black")
Nome1.configure(insertbackground="black")
Nome1.configure(selectbackground="blue")
Nome1.configure(selectforeground="white")

Idade = tk.Entry(Aumento)
Idade.place(relx=0.257, rely=0.2,height=20, relwidth=0.154)
Idade.configure(background="white")
Idade.configure(disabledforeground="#a3a3a3")
Idade.configure(font="TkFixedFont")
Idade.configure(foreground="#000000")
Idade.configure(highlightbackground="#d9d9d9")
Idade.configure(highlightcolor="black")
Idade.configure(insertbackground="black")
Idade.configure(selectbackground="blue")
Idade.configure(selectforeground="white")

Exp = tk.Entry(Aumento)
Exp.place(relx=0.257, rely=0.281,height=20, relwidth=0.154)
Exp.configure(background="white")
Exp.configure(disabledforeground="#a3a3a3")
Exp.configure(font="TkFixedFont")
Exp.configure(foreground="#000000")
Exp.configure(highlightbackground="#d9d9d9")
Exp.configure(highlightcolor="black")
Exp.configure(insertbackground="black")
Exp.configure(selectbackground="blue")
Exp.configure(selectforeground="white")

Salario = tk.Entry(Aumento)
Salario.place(relx=0.257, rely=0.361,height=20, relwidth=0.154)
Salario.configure(background="white")
Salario.configure(disabledforeground="#a3a3a3")
Salario.configure(font="TkFixedFont")
Salario.configure(foreground="#000000")
Salario.configure(highlightbackground="#d9d9d9")
Salario.configure(highlightcolor="black")
Salario.configure(insertbackground="black")
Salario.configure(selectbackground="blue")
Salario.configure(selectforeground="white")

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim Botões--------------------------------------------------------------------------#
#-----------------------------------------------Inicio Labels para inputs-----------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

txtfuncionario = tk.Label(Aumento)
txtfuncionario.place(relx=0.014, rely=0.02, height=21, width=140)
txtfuncionario.configure(activebackground="#f9f9f9")
txtfuncionario.configure(activeforeground="black")
#txtfuncionario.configure(background="#d9d9d9")
txtfuncionario.configure(disabledforeground="#a3a3a3")
txtfuncionario.configure(foreground="#000000")
txtfuncionario.configure(highlightbackground="#d9d9d9")
txtfuncionario.configure(highlightcolor="black")
txtfuncionario.configure(text='''Numero de Funcionarios:''')

txtfuncionario = tk.Label(Aumento)
txtfuncionario.place(relx=0.014, rely=0.02, height=21, width=140)
txtfuncionario.configure(activebackground="#f9f9f9")
txtfuncionario.configure(activeforeground="black")
#txtfuncionario.configure(background="#d9d9d9")
txtfuncionario.configure(disabledforeground="#a3a3a3")
txtfuncionario.configure(foreground="#000000")
txtfuncionario.configure(highlightbackground="#d9d9d9")
txtfuncionario.configure(highlightcolor="black")
txtfuncionario.configure(text='''Numero de Funcionarios:''')
tooltip_font = "TkDefaultFont"

txtnome2 = tk.Label(Aumento)
txtnome2.place(relx=0.100, rely=0.440, height=21, width=150)
txtnome2.configure(activebackground="#f9f9f9")
txtnome2.configure(activeforeground="black")
#txtnome2.configure(background="#d9d9d9")
txtnome2.configure(disabledforeground="#a3a3a3")
txtnome2.configure(foreground="#000000")
txtnome2.configure(highlightbackground="#d9d9d9")
txtnome2.configure(highlightcolor="black")
txtnome2.configure(text='''Selecione uma Formação:''')
tooltip_font = "TkDefaultFont"

txtnome = tk.Label(Aumento)
txtnome.place(relx=0.081, rely=0.12, height=21, width=42)
txtnome.configure(activebackground="#f9f9f9")
txtnome.configure(activeforeground="black")
#txtnome.configure(background="#d9d9d9")
txtnome.configure(disabledforeground="#a3a3a3")
txtnome.configure(foreground="#000000")
txtnome.configure(highlightbackground="#d9d9d9")
txtnome.configure(highlightcolor="black")
txtnome.configure(text='''Nome:''')

txtidade = tk.Label(Aumento)
txtidade.place(relx=0.081, rely=0.2, height=21, width=38)
txtidade.configure(activebackground="#f9f9f9")
txtidade.configure(activeforeground="black")
#txtidade.configure(background="#d9d9d9")
txtidade.configure(disabledforeground="#a3a3a3")
txtidade.configure(foreground="#000000")
txtidade.configure(highlightbackground="#d9d9d9")
txtidade.configure(highlightcolor="black")
txtidade.configure(text='''Idade:''')


txtexp = tk.Label(Aumento)
txtexp.place(relx=0.081, rely=0.281, height=21, width=68)
txtexp.configure(activebackground="#f9f9f9")
txtexp.configure(activeforeground="black")
#txtexp.configure(background="#d9d9d9")
txtexp.configure(disabledforeground="#a3a3a3")
txtexp.configure(foreground="#000000")
txtexp.configure(highlightbackground="#d9d9d9")
txtexp.configure(highlightcolor="black")
txtexp.configure(text='''Experiencia:''')

txtsalario = tk.Label(Aumento)
txtsalario.place(relx=0.081, rely=0.361, height=21, width=41)
txtsalario.configure(activebackground="#f9f9f9")
txtsalario.configure(activeforeground="black")
#txtsalario.configure(background="#d9d9d9")
txtsalario.configure(disabledforeground="#a3a3a3")
txtsalario.configure(foreground="#000000")
txtsalario.configure(highlightbackground="#d9d9d9")
txtsalario.configure(highlightcolor="black")
txtsalario.configure(text='''Salário''')

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim labels para inputs--------------------------------------------------------------#
#-----------------------------------------------Inicio Separadores------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#
from tkinter import ttk
TSeparator1 = ttk.Separator(Aumento)
TSeparator1.place(relx=0.0, rely=0.18, relwidth=0.418)

menubar = tk.Menu(Aumento,font="TkMenuFont",bg="#ff0000",fg="#ff0000")
Aumento.configure(menu = menubar)

TSeparator2 = ttk.Separator(Aumento)
TSeparator2.place(relx=-0.014, rely=0.1, relwidth=1.042)

TSeparator4 = ttk.Separator(Aumento)
TSeparator4.place(relx=0.419, rely=-0.02, relheight=1.042)
TSeparator4.configure(orient="vertical")

TSeparator5 = ttk.Separator(Aumento)
TSeparator5.place(relx=-0.072, rely=0.261, relwidth=0.488)

TSeparator6 = ttk.Separator(Aumento)
TSeparator6.place(relx=-0.015, rely=0.341, relwidth=0.432)

TSeparator7 = ttk.Separator(Aumento)
TSeparator7.place(relx=-0.041, rely=0.421, relwidth=0.461)

TSeparator8 = ttk.Separator(Aumento)
TSeparator8.place(relx=-0.29, rely=0.501, relwidth=0.708)

#-----------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Fim separadores---------------------------------------------------------------------#
#-----------------------------------------------Inicio Caixa de texto-----------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------#

Aumento.mainloop()
Login.mainloop()
