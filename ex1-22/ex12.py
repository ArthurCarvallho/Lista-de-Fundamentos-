### 12\. Menu interativo
from datetime import date
hoje = date.today()
data_formatada = hoje.strftime("%d/%m/%Y")
while True: 
    comando = int(input("Informe o que deseja fazer \n\n1 - Dizer olá \n2 - Mostrar data \n3 - Sair \n"))
    if comando == 1:
        print("Olá")
    elif comando == 2:
        print(data_formatada)
    elif comando == 3:
        print("Saindo...")
        break
    else:
        print("Comando não identificado")
     