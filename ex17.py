### 17\. Lista de compras
lista_produtos = []

def adicionar_produto(produto,lista_produtos):
    print("Produto adicionado com sucesso!\n")
    lista_produtos.append(produto)

def remover_produto(produto,lista_produtos):
    if produto in lista_produtos:
        lista_produtos.remove(produto)
        print("Produto removido com sucesso!\n")     
    else:
        print("Ops! O produto não está na lista!.")
        
       
def exibir_produtos(lista_produtos):
    if not lista_produtos:
        print("[A lista está vazia!]\n")
    else:
        print("\n" + "\n".join(lista_produtos) + "\n")
    
print("-------Lista de Compras---------\n\n")
    
while True:
    try:
        comando = int(input("O que deseja fazer: \n1 - Adicionar produto \n2 - Remover produto \n3 - Listar produtos \n4 - Sair \n"))
    except ValueError:
        print("\n\n Comando inválido, digite um número\n")
        continue
    if comando == 1:
        produto = input("Digite o produto: ")
        adicionar_produto(produto,lista_produtos)
    elif comando == 2:
        produto = input("Digite o produto: ")
        remover_produto(produto,lista_produtos)
    elif comando == 3:
        exibir_produtos(lista_produtos)
    elif comando == 4:
        print("Os produtos que ficaram na lista são:\n\n ")
        exibir_produtos(lista_produtos)
        print(":\n\n Saindo...")
        break
    else:
        print(":\n\n Comando não identificado, digite o comando corretamente!:\n\n ")
        
        