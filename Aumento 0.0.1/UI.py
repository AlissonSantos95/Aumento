import wx
from wx.lib import sized_controls
ID_Login = wx.NewId()
ID_Registro = wx.NewId()
ID_Sair = wx.NewId()
import simpleaudio as sa
from tkinter import *
import keyboard
from idlelib import window
import webbrowser
import Aumento_UI
url = "https://wwgoogle.com"
#adiciona titulo a tela  de boas vindas

def CreateWindow():
    window = Tk()
    #Botões que fazem parte da tela de boas vindas
    import simpleaudio as sa
    wave_obj = sa.WaveObject.from_wave_file("C:\Chord.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    lbl = Label(window, text="Bem Vindo", fg="black", font=("Arial", 23))#texto "bem vindo"
    lbl.place(x=180,y=250)# localização na tela do texto "bem vindo"

    lbl = Label(window, text="Aumento", fg="red", font=("Arial", 20))#texto "Aumento"
    lbl.place(x=200,y=300)# localização na tela do texto "Aumento"

    lbl = Label(window, text="Aperte para continuar", fg="black", font=("Arial", 20))# texto aperte para continuar
    lbl.place(x=130,y=380)# localização na tela do texto "Aperte para..."

    lbl = Button(window, text="login", command=window.destroy)#botao login
    lbl.place(x=245, y=430)# localização do botão "login"

    lbl1 = Button(window, text="Sair", command=execfile(Aumento))#botao login
    lbl1.place(x=245, y=480)# localização do botão "login"
    #----------------------------------------------------------------------------------
    window.title ("Aumento")
    #modifica o tamanho da tela de boas vindas
    window.geometry("500x600+100+200")
    window.mainloop()

class CustomDialog(sized_controls.SizedDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        pane = self.GetContentsPane()

        static_line = wx.StaticLine(pane, style=wx.LI_HORIZONTAL)
        static_line.SetSizerProps(border=(('all', 0)), expand=True)

        pane_btns = sized_controls.SizedPanel(pane)
        pane_btns.SetSizerType('horizontal')
        pane_btns.SetSizerProps(align='center')

        button_ok = wx.Button(pane_btns, ID_Login, label='Login')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        button_ok = wx.Button(pane_btns, ID_Registro, label='Registro')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        button_ok = wx.Button(pane_btns, ID_Sair, label='Sair')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        self.Fit()

    def on_button(self, event):
        if self.IsModal():
            self.EndModal(event.EventObject.Id)
        else:
            self.Close()



if __name__ == '__main__':
    CreateWindow()
    keyboard.is_pressed('esc')
    app = wx.App(False)
    dlg = CustomDialog(None, title='Custom Dialog')
    result = dlg.ShowModal()
    if result == ID_Login:
        print('Login')
        print("Login")
        login = input()
        print("senha:")
        senha = input()
        if senha != "admin":
             exit
        if login != "admin":
            exit
        print("Digite numero de funcionarios")
        funcionarios = input()
        print(funcionarios)
        import os
        os.system('cls')
        #-----------------------------------------
        while int(funcionarios) >= 1:
         if senha == "admin" :
             print("welcome")
             print("Aumento")
             print("Nome:")
             nome = input()
             print("idade")
             idade = input()
             print("formação")
             print ("F(fundamental), M(medio), S(superior), A(analfabeto), T(Tecnico)")
             #"F(fundamental), M(medio), S(superior), A(analfabeto), T(Tecnico)"
             formacao = input()
             print("Experiencia")
             experiencia = input()
             print("salario atual")
             salario = input()
             import os
             os.system('cls')
             if formacao == "F" :
               if int(idade) >= 18 or int(experiencia) >= 3:
                 aumento = float(salario) * 0.10
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "F" :
               if int(idade) < 18 and int(experiencia) < 3:
                 aumento = float(salario) * 0.05
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "M" :
               if int(idade) >= 20 or int(experiencia) >= 5:
                 aumento = float(salario) * 0.20
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "M" :
               if int(idade) < 20 and int(experiencia) < 5:
                 aumento = float(salario) * 0.10
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "T" :
               if int(idade) >= 25 or int(experiencia) >= 7:
                 aumento = float(salario) * 0.30
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "T" :
               if int(idade) < 25 and int(experiencia) < 7:
                 aumento = float(salario) * 0.20
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "S" :
               if int(idade) >= 30 or int(experiencia) >= 10:
                 aumento = float(salario) * 0.40
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "S" :
               if int(idade) < 18 and int(experiencia) < 10:
                 aumento = float(salario) * 0.30
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "A" :
               if int(idade) >= 40 or int(experiencia) >= 12:
                 aumento = float(salario) * 0.50
                 print("aumento de:")
                 print(aumento)
                 print("seu total é:")
                 print(float(salario)+float(aumento))
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
             if formacao == "A" :
               if int(idade) < 12 and int(experiencia) < 12:
                 aumento = float(salario) * 0.40
                 print("aumento de:")
                 print(aumento)
                 print("funcionarios restantes")
                 funcionarios = int(funcionarios) - 1
        if int(funcionarios) == 0:
           exit
        print(funcionarios)
    if result == ID_Sair:
        exit
    if result == ID_Registro:
        print("acesse http://www.aumento.com.br e se cadastre")
    dlg.Destroy()
    app.MainLoop()