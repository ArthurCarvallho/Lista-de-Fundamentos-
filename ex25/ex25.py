### 25\. Cadastro em arquivo
caminho = "./ex25/nomes.txt"
with open(caminho, "r") as arquivo:
        print(arquivo.read())


nome = input("Digite o nome que deseja salvar: ")

with open(caminho, "a") as arquivo:
    arquivo.write(nome)
    arquivo.write("\n")
    print("Nome salvo com sucesso!")
    