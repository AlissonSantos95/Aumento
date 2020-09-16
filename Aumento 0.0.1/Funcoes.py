#-------------------------------------------
#verificação de repetição, numero de funcionarios = numero de repetições
print("Digite numero de funcionarios")
funcionarios = input()
print(funcionarios)
import os
os.system('cls')
#-----------------------------------------
while int(funcionarios) >= 1:
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
           if int(funcionarios) == 0:
             exit
         if formacao == "F" :
          if int(idade) < 18 and int(experiencia) < 3:
           aumento = float(salario) * 0.05
           print("aumento de:")
           print(aumento)
           print("seu total é:")
           print(float(salario)+float(aumento))
           print("funcionarios restantes")
           funcionarios = int(funcionarios) - 1
           if int(funcionarios) == 0:
             exit
       if formacao == "M" :
        if int(idade) >= 20 or int(experiencia) >= 5:
         aumento = float(salario) * 0.20
         print("aumento de:")
         print(aumento)
         print("seu total é:")
         print(float(salario)+float(aumento))
         print("funcionarios restantes")
         funcionarios = int(funcionarios) - 1
         if int(funcionarios) == 0:
           exit
       if formacao == "M" :
        if int(idade) < 20 and int(experiencia) < 5:
          aumento = float(salario) * 0.10
          print("aumento de:")
          print(aumento)
          print("seu total é:")
          print(float(salario)+float(aumento))
          print("funcionarios restantes")
          funcionarios = int(funcionarios) - 1
          if int(funcionarios) == 0:
            exit
       if formacao == "T" :
        if int(idade) >= 25 or int(experiencia) >= 7:
          aumento = float(salario) * 0.30
          print("aumento de:")
          print(aumento)
          print("seu total é:")
          print(float(salario)+float(aumento))
          print("funcionarios restantes")
          funcionarios = int(funcionarios) - 1
          if int(funcionarios) == 0:
            exit
       if formacao == "T" :
         if int(idade) < 25 and int(experiencia) < 7:
           aumento = float(salario) * 0.20
           print("aumento de:")
           print(aumento)
           print("seu total é:")
           print(float(salario)+float(aumento))
           print("funcionarios restantes")
           funcionarios = int(funcionarios) - 1
           if int(funcionarios) == 0:
             exit
       if formacao == "S" :
          if int(idade) >= 30 or int(experiencia) >= 10:
           aumento = float(salario) * 0.40
           print("aumento de:")
           print(aumento)
           print("seu total é:")
           print(float(salario)+float(aumento))
           print("funcionarios restantes")
           funcionarios = int(funcionarios) - 1
           if int(funcionarios) == 0:
             exit
       if formacao == "S" :
         if int(idade) < 18 and int(experiencia) < 10:
          aumento = float(salario) * 0.30
          print("aumento de:")
          print(aumento)
          print("seu total é:")
          print(float(salario)+float(aumento))
          print("funcionarios restantes")
          funcionarios = int(funcionarios) - 1
          if int(funcionarios) == 0:
            exit
       if formacao == "A" :
         if int(idade) >= 40 or int(experiencia) >= 12:
           aumento = float(salario) * 0.50
           print("aumento de:")
           print(aumento)
           print("seu total é:")
           print(float(salario)+float(aumento))
           print("funcionarios restantes")
           funcionarios = int(funcionarios) - 1
           if int(funcionarios) == 0:
             exit
       if formacao == "A" :
         if int(idade) < 12 and int(experiencia) < 12:
           aumento = float(salario) * 0.40
           print("aumento de:")
           print(aumento)
           print("funcionarios restantes")
if int(funcionarios) == 0:
                   exit
