#Recebendo dados

nome = input("Digite seu nome?")
idade = int(input("Digite sua idade?"))
altura = float(input("Digite sua altura em centimetros?"))
cidade = input("Digite sua cidade?")

while True:
    cnh = input("Possui CNH?(responda com S para Sim e N para não)")
    
    if cnh.lower() == "s":
        cnh = True
        print(f"olá {nome}, os dados inseridos foram:\n{nome}\n{idade}\n{altura}\n{cidade}\n E informou que possui CNH.") 
        break
    elif cnh.lower() == "n":
        cnh = False
        print(f"olá {nome}, os dados inseridos foram:\n{nome}\n{idade}\n{altura}\n{cidade}\n E informou que não possui CNH.") 
        break
    else:
        print("O valor digitado é invalido")
        
