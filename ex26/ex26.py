### 26\. Diário

print("Bem-vindo ao Diário!")
caminho = "./ex26/diario.txt"
while True:
    try:
        comando = int(input("Digite o que deseja fazer (1- adicionar nova entrada 2- vizualizar diario 3- Sair)"))
        if comando == 1:
            data = input("Informe a data: ")  
            with open(caminho, "a") as arquivo:
                arquivo.write(data)
                arquivo.write("\n")
            entrada = input("Digite uma entrada: ")
            with open(caminho, "a") as arquivo:
                arquivo.write(entrada)
                arquivo.write("\n")
            print("Entrada salva com sucesso no diario!")
        elif comando == 2: 
            with open(caminho, "r") as arquivo:
                print(arquivo.read())
        elif comando == 3:
            print("Saindo...")
            break
                
            
    except: 
        print("Digite um comando valido!")
        continue
    

