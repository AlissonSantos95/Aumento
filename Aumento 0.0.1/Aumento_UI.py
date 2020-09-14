import wx
from wx.lib import sized_controls

ID_Login = wx.NewId()
ID_Registro = wx.NewId()
ID_Sair = wx.NewId()


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
