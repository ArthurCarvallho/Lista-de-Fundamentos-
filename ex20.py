### 21\. Cadastro de produtos

produtos = [
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 100},
    {"nome": "Monitor", "preco": 800}
]

def cadastrar_produto(nome, preco):
    nome_limpo = nome.strip().capitalize()
    preco_limpo = float(preco)
    novo_produto = { "nome": nome_limpo, "preco": preco_limpo}
         
    produtos.append(novo_produto)
    print(f"✅ Produto '{nome_limpo}' cadastrado com sucesso!")
    
def listar_produtos(produtos):
    print("--- LISTA DE PRODUTOS ---")
    for produto in produtos:
        print(f" Produto: {produto['nome']}  preço: R${produto['preco']:.2f}")

def buscar_produto(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f" Produto: {produto['nome']}  preço: R${produto['preco']:.2f}")
            return
    print("Produto não encontrado!")

def preco_total(produtos):
    soma = sum(produto["preco"] for produto in produtos)
    return soma
    

cadastrar_produto("Fone", 150)
listar_produtos(produtos)
buscar_produto("Mouse")
print(preco_total(produtos))