### 19\. Lista de alunos

alunos = ["Arthur", "Jorge", "Maria", "Julia", "Francisco"]

def adicionar_aluno(nome, alunos):
    alunos.append(nome)
    print("Aluno adicionado com Sucesso!")
    
def remover_aluno(nome, alunos):
    if nome in alunos:
        alunos.remove(nome)
        print("Aluno removido com sucesso")
    else:
        print("Aluno não econtrado no sistema")

def pesquisar_aluno(nome, alunos):
    if nome in alunos:
        print("Aluno encontrado!!!")
        
    else:
          print("Aluno não econtrado no sistema")
          
def mostrar_alunos(alunos):
    for aluno in alunos:
        print(f"{aluno}\n")


while True:
    try:
        comando = int(input("O que deseja fazer: \n1 - Adicionar Aluno \n2 - Remover Aluno \n3 - pesquisar Aluno \n4 - Mostrar alunos\n 5 - Sair"))
    except ValueError:
        print("\n\n Comando inválido, digite um número\n")
        continue
    if comando == 1:
        nome = input("Digite nome do aluno: ")
        adicionar_aluno(nome, alunos)
    elif comando == 2:
        nome = input("Digite o nome do aluno: ")
        remover_aluno(nome, alunos)
    elif comando == 3:
        nome = input("Digite o nome do aluno: ")
        pesquisar_aluno(nome, alunos)
    elif comando == 4:
        mostrar_alunos(alunos)
    elif comando == 5:
        print("Os alunos que ficaram na lista são:\n\n ")
        mostrar_alunos(alunos)
        print(":\n\n Saindo...")
        break
    else:
        print(":\n\n Comando não identificado, digite o comando corretamente!:\n\n ")
        