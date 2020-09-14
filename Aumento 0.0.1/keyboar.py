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

    lbl = Button(window, text="Sair", command=window.destroy, command= lambda: execfile("Aumento_UI.py"))#botao login
    lbl.place(x=245, y=480)# localização do botão "login"
    #----------------------------------------------------------------------------------
    window.title ("Aumento")
    #modifica o tamanho da tela de boas vindas
    window.geometry("500x600+100+200")
    window.mainloop()

if __name__ == '__main__':
    CreateWindow()